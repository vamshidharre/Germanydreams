import re

file_path = r'd:\GermanyDreams\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero Avatar with Badges
avatar_target = """<div class="avatar-ring">
            <img src="Profile_pictur.jpg" alt="Vamshidhar Reddy"
              style="width:100%; height:100%; object-fit:cover; border-radius:50%;" />
          </div>"""

avatar_replacement = """<div class="hero-avatar-wrapper" style="position: relative; display: inline-block;">
            <div class="floating-badge fb-1">
              <span style="font-size: 1.2rem;">🎥</span> 5K+ Subs
            </div>
            <div class="floating-badge fb-2">
              <span style="font-size: 1.2rem;">🎓</span> FAU Student
            </div>
            <div class="avatar-ring">
              <img src="Profile_pictur.jpg" alt="Vamshidhar Reddy"
                style="width:100%; height:100%; object-fit:cover; border-radius:50%; z-index: 2; position: relative;" />
            </div>
          </div>"""

if avatar_target in html:
    html = html.replace(avatar_target, avatar_replacement)
else:
    print("Could not find avatar_target")

# 2. Add Magnetic Wrapper to Youtube Button
btn_target = """<a class="btn-youtube" href="https://www.youtube.com/channel/UCIY3viuqfg8BR9ucyCI2e1w" target="_blank">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.5 12 3.5 12 3.5s-7.505 0-9.377.55a3.016 3.016 0 0 0-2.122 2.136C0 8.057 0 12 0 12s0 3.943.501 5.814a3.016 3.016 0 0 0 2.122 2.136c1.872.55 9.377.55 9.377.55s7.505 0 9.377-.55a3.016 3.016 0 0 0 2.122-2.136C24 15.943 24 12 24 12s0-3.943-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            Watch on YouTube
          </a>"""
btn_replacement = """<div class="magnetic-wrap">
            <a class="btn-youtube" href="https://www.youtube.com/channel/UCIY3viuqfg8BR9ucyCI2e1w" target="_blank">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.5 12 3.5 12 3.5s-7.505 0-9.377.55a3.016 3.016 0 0 0-2.122 2.136C0 8.057 0 12 0 12s0 3.943.501 5.814a3.016 3.016 0 0 0 2.122 2.136c1.872.55 9.377.55 9.377.55s7.505 0 9.377-.55a3.016 3.016 0 0 0 2.122-2.136C24 15.943 24 12 24 12s0-3.943-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
              Watch on YouTube
            </a>
          </div>"""
if btn_target in html:
    html = html.replace(btn_target, btn_replacement)
else:
    print("Could not find btn_target")

# 3. Add background grid
hero_orb = '<div class="hero-orb hero-orb-1"></div>'
grid_html = '<div class="hero-grid"></div>\n    <div class="hero-orb hero-orb-1"></div>'
if hero_orb in html:
    html = html.replace(hero_orb, grid_html)
else:
    print("Could not find hero_orb")

# 4. Inject CSS
css_injections = """
    /* --- PREMIUM UPGRADES --- */
    
    /* Grid Background in Hero */
    .hero-grid {
      position: absolute;
      inset: 0;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.04) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
      background-size: 60px 60px;
      mask-image: radial-gradient(circle at center, black 0%, transparent 80%);
      -webkit-mask-image: radial-gradient(circle at center, black 0%, transparent 80%);
      pointer-events: none;
      z-index: 0;
      animation: gridMove 25s linear infinite;
    }

    @keyframes gridMove {
      0% { transform: translateY(0); }
      100% { transform: translateY(60px); }
    }

    /* Floating Badges */
    .floating-badge {
      position: absolute;
      background: rgba(15, 31, 53, 0.7);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 100px;
      padding: 0.6rem 1.2rem;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 0.6rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      z-index: 10;
      white-space: nowrap;
    }

    .fb-1 {
      top: -10px;
      left: -60px;
      animation: floatObj 6s ease-in-out infinite;
    }

    .fb-2 {
      bottom: 10px;
      right: -60px;
      animation: floatObj 5s ease-in-out infinite alternate-reverse;
      background: rgba(14, 165, 176, 0.15);
      border-color: rgba(14, 165, 176, 0.3);
      color: var(--accent2);
    }

    @keyframes floatObj {
      0%, 100% { transform: translateY(0) rotate(-2deg); }
      50% { transform: translateY(-12px) rotate(2deg); }
    }

    /* Magnetic Button Wrapper */
    .magnetic-wrap {
      display: inline-block;
      position: relative;
    }

    /* Premium Glow on Cards */
    .pillar-card, .resource-link {
      background: linear-gradient(145deg, var(--card), rgba(15, 31, 53, 0.4));
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .pillar-card:hover, .resource-link:hover {
      background: linear-gradient(145deg, var(--card), rgba(14, 165, 176, 0.08));
      border-color: rgba(14, 165, 176, 0.4);
      box-shadow: 0 15px 35px rgba(14, 165, 176, 0.15);
    }

    /* Avatar Conic Spinning Glow Fix */
    .avatar-ring {
      width: 120px !important;
      height: 120px !important;
      border-radius: 50% !important;
      position: relative;
      background: none !important;
      box-shadow: none !important;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 1.5rem;
      z-index: 1;
    }

    .avatar-ring::before {
      content: '';
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      background: conic-gradient(from 0deg, transparent, var(--accent), var(--gold), transparent 60%);
      animation: spinBorder 3s linear infinite;
      z-index: 0;
    }

    .avatar-ring::after {
      content: '';
      position: absolute;
      inset: 0px;
      background: var(--card);
      border-radius: 50%;
      z-index: 1;
    }

    .avatar-ring img {
      position: relative;
      z-index: 2;
      border: 4px solid var(--card);
    }

    @keyframes spinBorder {
      100% { transform: rotate(360deg); }
    }
"""
if "/* NAV */" in html:
    html = html.replace('/* NAV */', css_injections + '\n    /* NAV */')
else:
    print("Could not find /* NAV */ for CSS injection")

# 5. Inject JS
js_injection = """
    // Magnetic Button Effect
    const magneticBtns = document.querySelectorAll('.magnetic-wrap');
    magneticBtns.forEach(btn => {
      btn.addEventListener('mousemove', function(e) {
        const position = btn.getBoundingClientRect();
        const x = e.clientX - position.left - position.width / 2;
        const y = e.clientY - position.top - position.height / 2;
        
        btn.children[0].style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
      });
      
      btn.addEventListener('mouseleave', function() {
        btn.children[0].style.transform = 'translate(0px, 0px)';
        btn.children[0].style.transition = 'transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
      });
      
      btn.addEventListener('mouseenter', function() {
        btn.children[0].style.transition = 'none';
      });
    });
"""
if "// Nav active link highlight on scroll" in html:
    html = html.replace('// Nav active link highlight on scroll', js_injection + '\n    // Nav active link highlight on scroll')
else:
    print("Could not find JS insertion point")


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied successfully.")
