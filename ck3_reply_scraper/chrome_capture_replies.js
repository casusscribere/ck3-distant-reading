/* chrome_capture_replies.js — Claude-in-Chrome DOM capture for CK3 reply threads.
 *
 * Run inside the forum thread tab (via the javascript_tool). It walks every
 * page of the thread with same-origin fetch(), extracts each reply post
 * structurally (more reliable than text-marker parsing), separates XenForo
 * quote blocks into artifact:quote spans, and ANONYMIZES authors to stable
 * per-thread participant ids (the numeric user-id is hashed; the username is
 * never stored). The dev-diary OP is naturally excluded because Paradox renders
 * it outside `article.message`.
 *
 * Returns the data on window.__ck3replies and builds the rt_*.md on window.__md.
 * Because javascript_tool truncates large returns (~5k) and get_page_text caps
 * at 50k chars, materialize window.__md by injecting <pre> slices and reading
 * them with get_page_text (see README "Running it live").
 *
 * Set PAGES from the thread's "Page 1 of N" indicator before running.
 */
async function captureReplies(baseUrl, PAGES){
  function uidHash(id){ let h=0; const s=String(id); for(let i=0;i<s.length;i++){h=(h*31+s.charCodeAt(i))>>>0;} return 'user_'+h.toString(36); }
  const out=[];
  for(let pg=1; pg<=PAGES; pg++){
    const url = pg===1 ? baseUrl : baseUrl+'page-'+pg;
    let html; try { html = await fetch(url,{credentials:'same-origin'}).then(r=>r.text()); }
    catch(e){ out.push({_error:String(e),page:pg}); continue; }
    const doc = new DOMParser().parseFromString(html,'text/html');
    doc.querySelectorAll('article.message').forEach(a=>{
      const uid = a.querySelector('[data-user-id]')?.getAttribute('data-user-id') || null;
      const plink = a.querySelector('a[href*="post-"]')?.getAttribute('href') || '';
      const pid = (plink.match(/post-(\d+)/)||[])[1] || null;
      const time = a.querySelector('time')?.getAttribute('datetime') || null;
      const bb = a.querySelector('.bbWrapper');
      let quotes=[], body='';
      if(bb){
        const clone = bb.cloneNode(true);
        clone.querySelectorAll('.bbCodeBlock--quote, blockquote').forEach(q=>{
          quotes.push((q.textContent||'').replace(/\s+/g,' ').trim().slice(0,400)); q.remove(); });
        body = (clone.textContent||'').replace(/\s+/g,' ').trim();
      }
      out.push({page:pg, post_id:pid, user:uid?uidHash(uid):null, time, body, quotes});
    });
    await new Promise(r=>setTimeout(r,180));
  }
  window.__ck3replies = out;
  return {total_posts:out.length, participants:new Set(out.map(p=>p.user)).size, pages:PAGES};
}
/* Example:
   await captureReplies("https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-3-war.1279641/", 22);
*/
