import sys
import re

file_path = r'd:\GermanyDreams\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
css_start = '    /* CONNECT */'
css_end = '    /* FOOTER */'
css_pattern = re.compile(rf'{re.escape(css_start)}.*?{re.escape(css_end)}', re.DOTALL)

css_replacement = '''    /* CONNECT & GROW */
    #connect {
      background: var(--bg2);
      position: relative;
    }

    .connect-bento {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin-top: 2rem;
    }

    .bento-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 2.2rem;
      position: relative;
      overflow: hidden;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 240px;
      text-decoration: none;
      color: var(--text);
      z-index: 1;
    }

    .bento-card:hover {
      transform: translateY(-8px);
      box-shadow: 0 15px 40px rgba(0,0,0,0.4);
      border-color: rgba(14, 165, 176, 0.4);
    }

    .bento-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: linear-gradient(90deg, transparent, var(--accent), transparent);
      opacity: 0;
      transition: opacity 0.3s;
      z-index: 2;
    }
    
    .bento-card:hover::before {
      opacity: 1;
    }

    .bento-card::after {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at top right, rgba(14,165,176,0.08) 0%, transparent 60%);
      opacity: 0;
      transition: opacity 0.3s;
      z-index: -1;
    }
    
    .bento-card:hover::after {
      opacity: 1;
    }

    .bc-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 2rem;
    }

    .bc-icon {
      width: 60px;
      height: 60px;
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2rem;
      background: var(--card2);
      transition: transform 0.3s;
    }

    .bento-card:hover .bc-icon {
      transform: scale(1.1) rotate(-5deg);
    }

    .bc-arrow {
      color: var(--muted);
      font-size: 1.2rem;
      transition: transform 0.3s, color 0.3s;
    }

    .bento-card:hover .bc-arrow {
      transform: translate(5px, -5px);
      color: var(--accent);
    }

    .bc-content h3 {
      font-family: 'Syne', sans-serif;
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 0.6rem;
    }

    .bc-content p {
      font-size: 0.95rem;
      color: var(--muted);
      line-height: 1.6;
    }

    .bc-yt .bc-icon { color: #ff0000; background: rgba(255,0,0,0.1); }
    .bc-ig .bc-icon { color: #e1306c; background: rgba(225,48,108,0.1); }
    .bc-li .bc-icon { color: #0077b5; background: rgba(0,119,181,0.1); }
    .bc-wa .bc-icon { color: #25d366; background: rgba(37,211,102,0.1); }
    .bc-tg .bc-icon { color: #0088cc; background: rgba(0,136,204,0.1); }

    .bento-newsletter {
      grid-column: 1 / -1;
      background: linear-gradient(135deg, var(--card), var(--card2));
      border: 1px solid var(--accent);
      border-radius: 24px;
      padding: 3rem;
      min-height: auto;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3rem;
      align-items: center;
      box-shadow: 0 0 30px rgba(14,165,176,0.1);
    }

    .nl-info h3 {
      font-family: 'Syne', sans-serif;
      font-size: 2.2rem;
      font-weight: 800;
      margin-bottom: 1rem;
      background: linear-gradient(90deg, #fff, var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      letter-spacing: -0.02em;
    }

    .nl-info p {
      color: var(--muted);
      font-size: 1rem;
      line-height: 1.7;
      margin-bottom: 0;
    }

    .nl-form-wrap {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .nl-form {
      display: flex;
      gap: 0.8rem;
    }

    .nl-input {
      flex: 1;
      background: var(--bg);
      border: 1px solid var(--border);
      padding: 1rem 1.5rem;
      border-radius: 14px;
      color: var(--text);
      font-family: inherit;
      font-size: 1rem;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }

    .nl-input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 4px rgba(14,165,176,0.15);
    }

    .nl-btn {
      background: var(--accent);
      color: #fff;
      border: none;
      padding: 1rem 2rem;
      border-radius: 14px;
      font-family: 'Syne', sans-serif;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
      white-space: nowrap;
    }

    .nl-btn:hover {
      background: var(--accent2);
      transform: translateY(-2px);
      box-shadow: 0 5px 20px rgba(14,165,176,0.4);
    }

    .nl-note {
      font-size: 0.8rem;
      color: var(--muted);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .nl-note span {
      color: #22c55e;
    }

    @media (max-width: 860px) {
      .bento-newsletter {
        grid-template-columns: 1fr;
        padding: 2.5rem 1.5rem;
        gap: 2rem;
      }
      .nl-form {
        flex-direction: column;
      }
      .nl-btn {
        width: 100%;
      }
    }

    /* FOOTER */'''

new_content = css_pattern.sub(css_replacement, content)

# Replace HTML
html_start = '  <!-- CONNECT -->'
html_end = '  <!-- FOOTER -->'
html_pattern = re.compile(rf'{re.escape(html_start)}.*?{re.escape(html_end)}', re.DOTALL)

html_replacement = '''  <!-- CONNECT & GROW -->
  <section id="connect">
    <div class="section-inner">
      <div class="section-label reveal">Community &amp; Reach</div>
      <h2 class="section-title reveal">Let's Connect &amp; Grow</h2>
      <p class="section-desc reveal">Join thousands of students on the same journey. Need advice, looking for a study group, or just want to follow the vlogs? Jump in.</p>
      
      <div class="connect-bento inline-reveal">
        
        <!-- YOUTUBE -->
        <a class="bento-card bc-yt reveal" href="https://www.youtube.com/channel/UCIY3viuqfg8BR9ucyCI2e1w" target="_blank">
          <div class="bc-header">
            <div class="bc-icon">
              <!-- Inline YouTube SVG -->
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.5 12 3.5 12 3.5s-7.505 0-9.377.55a3.016 3.016 0 0 0-2.122 2.136C0 8.057 0 12 0 12s0 3.943.501 5.814a3.016 3.016 0 0 0 2.122 2.136c1.872.55 9.377.55 9.377.55s7.505 0 9.377-.55a3.016 3.016 0 0 0 2.122-2.136C24 15.943 24 12 24 12s0-3.943-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            </div>
            <div class="bc-arrow">&#8599;</div>
          </div>
          <div class="bc-content">
            <h3>YouTube Channel</h3>
            <p>Weekly vlogs, detailed guides, and authentic stories from my life as a student in Stuttgart.</p>
          </div>
        </a>

        <!-- INSTAGRAM -->
        <a class="bento-card bc-ig reveal" href="#" target="_blank">
          <div class="bc-header">
            <div class="bc-icon">
              <!-- Instagram SVG -->
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
            </div>
            <div class="bc-arrow">&#8599;</div>
          </div>
          <div class="bc-content">
            <h3>Instagram</h3>
            <p>Daily updates, quick tips in Reels, and behind-the-scenes of campus life.</p>
          </div>
        </a>

        <!-- LINKEDIN -->
        <a class="bento-card bc-li reveal" href="https://www.linkedin.com/in/vamshidhar-reddy-7180551a2/" target="_blank">
          <div class="bc-header">
            <div class="bc-icon">
              <!-- LinkedIn SVG -->
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
            </div>
            <div class="bc-arrow">&#8599;</div>
          </div>
          <div class="bc-content">
            <h3>LinkedIn</h3>
            <p>Let's connect professionally. Follow my engineering career and application advice.</p>
          </div>
        </a>

        <!-- COMMUNITY / WHATSAPP -->
        <a class="bento-card bc-wa reveal" href="#" target="_blank">
          <div class="bc-header">
            <div class="bc-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
            </div>
            <div class="bc-arrow">&#8599;</div>
          </div>
          <div class="bc-content">
            <h3>WhatsApp Community</h3>
            <p>Join our active student group. Ask doubts, find roommates, and stay updated together.</p>
          </div>
        </a>

        <!-- NEWSLETTER OPT-IN (Takes 2 columns ideally) -->
        <div class="bento-card bento-newsletter reveal">
          <div class="nl-info">
            <h3>The Germany Newsletter</h3>
            <p>Get my best tips delivered straight to your inbox every month. No spam, only high-value resources, scholarship updates, and exclusive guides.</p>
          </div>
          <div class="nl-form-wrap">
            <form class="nl-form" onsubmit="event.preventDefault(); alert('Thanks for subscribing! Please check your email inbox to confirm.');">
              <input type="email" class="nl-input" placeholder="Your best email address" required>
              <button type="submit" class="nl-btn">Join 5K+ Students</button>
            </form>
            <div class="nl-note">
              <span>&#10003;</span> 100% Free. Unsubscribe completely anytime.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->'''

new_content = html_pattern.sub(html_replacement, new_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("done")
