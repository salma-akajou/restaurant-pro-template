import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\about.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

sections = re.split(r'(<section.*?</section>)', content, flags=re.DOTALL)

target_idx = -1
for i, sec in enumerate(sections):
    if 'data-i18n="about-soul-title"' in sec:
        target_idx = i
        break

if target_idx != -1:
    new_gallery_and_community = """
    <!-- ================= EDITORIAL GALLERY SECTION ================= -->
    <section class="py-24 md:py-32 bg-[#050505] overflow-hidden relative border-t border-white/5" id="editorial-gallery">
        <!-- Glow effect -->
        <div class="absolute left-1/2 top-0 -translate-x-1/2 w-[800px] h-[400px] bg-primary/5 blur-[120px] rounded-full pointer-events-none z-0"></div>
        
        <div class="w-full max-w-7xl mx-auto px-4 relative z-10">
            <div class="text-center mb-16 fade-up">
                <p class="text-[10px] md:text-xs text-primary tracking-[0.2em] uppercase font-bold mb-4" data-i18n="about-soul-eyebrow">Editorial Gallery</p>
                <h2 class="font-serif text-3xl md:text-5xl lg:text-5xl text-white mb-4" data-i18n="about-soul-title">L'âme de Maison Lumière</h2>
                <div class="flex items-center justify-center gap-2 opacity-80">
                    <div class="h-px w-6 bg-primary"></div>
                    <div class="w-1 h-1 rotate-45 bg-primary"></div>
                    <div class="h-px w-6 bg-primary"></div>
                </div>
            </div>
        </div>
        
        <!-- Gallery Container -->
        <div class="relative w-full h-[500px] md:h-[600px] group mt-8 z-10" id="gallery-wrapper">
            <!-- Floating Buttons -->
            <button id="gallery-prev" class="absolute left-4 md:left-12 top-1/2 -translate-y-1/2 z-50 w-12 h-12 rounded-full bg-black/40 backdrop-blur-md border border-[#C1A58D]/30 flex items-center justify-center text-white/70 hover:text-[#C1A58D] hover:bg-black/60 hover:border-[#C1A58D]/80 hover:scale-105 transition-all duration-300 shadow-lg shadow-black/50 opacity-0 group-hover:opacity-100">
                <i data-lucide="chevron-left" class="w-6 h-6"></i>
            </button>
            <button id="gallery-next" class="absolute right-4 md:right-12 top-1/2 -translate-y-1/2 z-50 w-12 h-12 rounded-full bg-black/40 backdrop-blur-md border border-[#C1A58D]/30 flex items-center justify-center text-white/70 hover:text-[#C1A58D] hover:bg-black/60 hover:border-[#C1A58D]/80 hover:scale-105 transition-all duration-300 shadow-lg shadow-black/50 opacity-0 group-hover:opacity-100">
                <i data-lucide="chevron-right" class="w-6 h-6"></i>
            </button>
            
            <!-- Track -->
            <div id="gallery-track" class="flex items-center h-full gap-4 md:gap-8 px-4 w-max cursor-grab active:cursor-grabbing">
                <!-- Items -->
                <div class="gallery-item w-[260px] md:w-[350px] h-[340px] md:h-[450px] rounded-[24px] overflow-hidden shrink-0 relative transform md:-translate-y-8 shadow-[0_20px_40px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=600&q=80" alt="Ambiance" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="gallery-item w-[320px] md:w-[450px] h-[380px] md:h-[500px] rounded-[24px] overflow-hidden shrink-0 relative transform md:translate-y-4 shadow-[0_20px_40px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=800&q=80" alt="Cocktail" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="gallery-item w-[240px] md:w-[300px] h-[300px] md:h-[400px] rounded-[24px] overflow-hidden shrink-0 relative transform md:-translate-y-12 shadow-[0_20px_40px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=500&q=80" alt="Planche" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="gallery-item w-[300px] md:w-[400px] h-[340px] md:h-[480px] rounded-[24px] overflow-hidden shrink-0 relative transform md:translate-y-8 shadow-[0_20px_40px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=700&q=80" alt="Plat Signature" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="gallery-item w-[260px] md:w-[350px] h-[320px] md:h-[420px] rounded-[24px] overflow-hidden shrink-0 relative transform md:-translate-y-2 shadow-[0_20px_40px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=600&q=80" alt="Dessert" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="gallery-item w-[340px] md:w-[480px] h-[380px] md:h-[520px] rounded-[24px] overflow-hidden shrink-0 relative transform md:translate-y-6 shadow-[0_20px_40px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=800&q=80" alt="Restaurant Interieur" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
            </div>
        </div>
    </section>

    <!-- ================= COMMUNITY SECTION ================= -->
    <section class="py-24 md:py-32 bg-[#0a0a0a] relative overflow-hidden">
        <!-- Glow effect -->
        <div class="absolute right-0 bottom-0 w-[600px] h-[600px] bg-primary/5 blur-[150px] rounded-full pointer-events-none"></div>
        <div class="absolute left-0 top-0 w-[400px] h-[400px] bg-white/5 blur-[120px] rounded-full pointer-events-none"></div>

        <!-- Decorative Lines -->
        <div class="absolute top-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-primary/20 to-transparent"></div>

        <div class="max-w-7xl mx-auto px-6 relative z-10">
            <div class="text-center mb-20 fade-up">
                <h2 class="font-serif text-3xl md:text-5xl lg:text-5xl text-white mb-6 font-bold">Notre Communauté</h2>
                <p class="text-sm md:text-base text-gray-400 max-w-2xl mx-auto font-light italic">
                    "Des milliers de passionnés suivent chaque instant de Maison Lumière."
                </p>
                <div class="flex items-center justify-center gap-2 opacity-80 mt-8">
                    <div class="h-px w-6 bg-primary"></div>
                    <div class="w-1 h-1 rotate-45 bg-primary"></div>
                    <div class="h-px w-6 bg-primary"></div>
                </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Instagram -->
                <div class="group flex flex-col items-center justify-center p-10 rounded-[24px] bg-[#050505] border border-[#C1A58D]/20 shadow-lg hover:-translate-y-2 hover:shadow-[0_0_30px_rgba(193,165,141,0.15)] transition-all duration-700 ease-out relative overflow-hidden fade-up">
                    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>
                    <i data-lucide="instagram" class="w-8 h-8 text-white mb-8 group-hover:text-primary transition-colors duration-500"></i>
                    <h3 class="text-xs text-gray-400 tracking-[0.2em] uppercase mb-2">Instagram</h3>
                    <div class="font-serif text-3xl md:text-4xl text-white mb-2 transition-all duration-700 group-hover:brightness-125">42.8K</div>
                    <div class="text-[10px] text-[#C1A58D] mb-8 tracking-widest">+12% CE MOIS</div>
                    <a href="#" class="px-6 py-2 rounded-full border border-white/20 text-xs text-white/80 hover:text-white hover:border-primary hover:bg-primary/10 transition-colors duration-300 z-10">Visiter</a>
                </div>

                <!-- Facebook -->
                <div class="group flex flex-col items-center justify-center p-10 rounded-[24px] bg-[#050505] border border-[#C1A58D]/20 shadow-lg hover:-translate-y-2 hover:shadow-[0_0_30px_rgba(193,165,141,0.15)] transition-all duration-700 ease-out relative overflow-hidden fade-up" style="transition-delay: 100ms">
                    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>
                    <i data-lucide="facebook" class="w-8 h-8 text-white mb-8 group-hover:text-primary transition-colors duration-500"></i>
                    <h3 class="text-xs text-gray-400 tracking-[0.2em] uppercase mb-2">Facebook</h3>
                    <div class="font-serif text-3xl md:text-4xl text-white mb-2 transition-all duration-700 group-hover:brightness-125">18.4K</div>
                    <div class="text-[10px] text-[#C1A58D] mb-8 tracking-widest">+5% CE MOIS</div>
                    <a href="#" class="px-6 py-2 rounded-full border border-white/20 text-xs text-white/80 hover:text-white hover:border-primary hover:bg-primary/10 transition-colors duration-300 z-10">Visiter</a>
                </div>

                <!-- TikTok -->
                <div class="group flex flex-col items-center justify-center p-10 rounded-[24px] bg-[#050505] border border-[#C1A58D]/20 shadow-lg hover:-translate-y-2 hover:shadow-[0_0_30px_rgba(193,165,141,0.15)] transition-all duration-700 ease-out relative overflow-hidden fade-up" style="transition-delay: 200ms">
                    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-8 h-8 text-white mb-8 group-hover:text-primary transition-colors duration-500"><path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5"/><path d="M15 8a4 4 0 1 0 0-8"/></svg>
                    <h3 class="text-xs text-gray-400 tracking-[0.2em] uppercase mb-2">TikTok</h3>
                    <div class="font-serif text-3xl md:text-4xl text-white mb-2 transition-all duration-700 group-hover:brightness-125">95.2K</div>
                    <div class="text-[10px] text-[#C1A58D] mb-8 tracking-widest">+28% CE MOIS</div>
                    <a href="#" class="px-6 py-2 rounded-full border border-white/20 text-xs text-white/80 hover:text-white hover:border-primary hover:bg-primary/10 transition-colors duration-300 z-10">Visiter</a>
                </div>

                <!-- TripAdvisor -->
                <div class="group flex flex-col items-center justify-center p-10 rounded-[24px] bg-[#050505] border border-[#C1A58D]/20 shadow-lg hover:-translate-y-2 hover:shadow-[0_0_30px_rgba(193,165,141,0.15)] transition-all duration-700 ease-out relative overflow-hidden fade-up" style="transition-delay: 300ms">
                    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-8 h-8 text-white mb-8 group-hover:text-primary transition-colors duration-500"><circle cx="8" cy="10" r="3"/><circle cx="16" cy="10" r="3"/><path d="M12 21a9 9 0 0 0 9-9c0-1.8-1.5-4-3.5-4h-11C4.5 8 3 10.2 3 12a9 9 0 0 0 9 9Z"/><path d="M12 14v7"/></svg>
                    <h3 class="text-xs text-gray-400 tracking-[0.2em] uppercase mb-2">TripAdvisor</h3>
                    <div class="font-serif text-3xl md:text-4xl text-white mb-2 transition-all duration-700 group-hover:brightness-125">4.9<span class="text-primary text-2xl ml-1">★</span></div>
                    <div class="text-[10px] text-gray-400 mb-8 tracking-widest uppercase">3 400 avis</div>
                    <a href="#" class="px-6 py-2 rounded-full border border-white/20 text-xs text-white/80 hover:text-white hover:border-primary hover:bg-primary/10 transition-colors duration-300 z-10">Visiter</a>
                </div>
            </div>
        </div>
    </section>
"""

    sections[target_idx] = new_gallery_and_community
    
    # Let's write the JS script
    js_script = """
    <!-- Editorial Gallery JS -->
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        const track = document.getElementById('gallery-track');
        if (track) {
            // Clone items for infinite scroll
            const items = Array.from(track.children);
            items.forEach(item => {
                const clone = item.cloneNode(true);
                track.appendChild(clone);
            });
            
            // To ensure seamless scroll we can even clone them twice to be super safe
            items.forEach(item => {
                const clone = item.cloneNode(true);
                track.appendChild(clone);
            });

            let scrollSpeed = 0.8; 
            let currentPos = 0;
            let isPaused = false;
            let rafId;
            let speedMultiplier = 1;
            let targetSpeedMultiplier = 1;

            function scroll() {
                if (!isPaused) {
                    speedMultiplier += (targetSpeedMultiplier - speedMultiplier) * 0.05;
                    currentPos += scrollSpeed * speedMultiplier;
                    
                    // We cloned items twice, so scrollWidth is 3x original.
                    // When we reach 1/3 of scrollWidth, reset to 0
                    if (currentPos >= track.scrollWidth / 3) {
                        currentPos = 0;
                    }
                    
                    track.style.transform = `translate3d(-${currentPos}px, 0, 0)`;
                }
                rafId = requestAnimationFrame(scroll);
            }

            scroll();

            // Hover effect to slow down
            const wrapper = document.getElementById('gallery-wrapper');
            if(wrapper) {
                wrapper.addEventListener('mouseenter', () => {
                    targetSpeedMultiplier = 0.2; 
                });
                wrapper.addEventListener('mouseleave', () => {
                    targetSpeedMultiplier = 1; 
                });
            }

            // Drag to scroll
            let isDragging = false;
            let startX;
            let scrollLeft;

            track.addEventListener('mousedown', (e) => {
                isDragging = true;
                isPaused = true;
                startX = e.pageX - track.offsetLeft;
                scrollLeft = currentPos;
                track.style.cursor = 'grabbing';
                cancelAnimationFrame(rafId);
            });

            track.addEventListener('mouseleave', () => {
                if(isDragging) {
                    isDragging = false;
                    isPaused = false;
                    track.style.cursor = 'grab';
                    scroll();
                }
            });

            track.addEventListener('mouseup', () => {
                isDragging = false;
                isPaused = false;
                track.style.cursor = 'grab';
                scroll();
            });

            track.addEventListener('mousemove', (e) => {
                if (!isDragging) return;
                e.preventDefault();
                const x = e.pageX - track.offsetLeft;
                const walk = (x - startX) * 1.5;
                currentPos = scrollLeft - walk;
                
                if (currentPos < 0) currentPos += track.scrollWidth / 3;
                if (currentPos >= track.scrollWidth / 3) currentPos -= track.scrollWidth / 3;
                
                track.style.transform = `translate3d(-${currentPos}px, 0, 0)`;
            });
            
            // Touch events for mobile
            track.addEventListener('touchstart', (e) => {
                isDragging = true;
                isPaused = true;
                startX = e.touches[0].pageX - track.offsetLeft;
                scrollLeft = currentPos;
                cancelAnimationFrame(rafId);
            });
            
            track.addEventListener('touchend', () => {
                isDragging = false;
                isPaused = false;
                scroll();
            });
            
            track.addEventListener('touchmove', (e) => {
                if (!isDragging) return;
                const x = e.touches[0].pageX - track.offsetLeft;
                const walk = (x - startX) * 1.5;
                currentPos = scrollLeft - walk;
                
                if (currentPos < 0) currentPos += track.scrollWidth / 3;
                if (currentPos >= track.scrollWidth / 3) currentPos -= track.scrollWidth / 3;
                
                track.style.transform = `translate3d(-${currentPos}px, 0, 0)`;
            });

            // Prev/Next Buttons
            const btnPrev = document.getElementById('gallery-prev');
            const btnNext = document.getElementById('gallery-next');

            if (btnPrev && btnNext) {
                btnPrev.addEventListener('click', () => {
                    let targetPos = currentPos - 400;
                    if (targetPos < 0) targetPos += track.scrollWidth / 3;
                    
                    // animate manually
                    track.style.transition = 'transform 0.5s ease-out';
                    track.style.transform = `translate3d(-${targetPos}px, 0, 0)`;
                    currentPos = targetPos;
                    
                    // restore fast
                    setTimeout(() => {
                        track.style.transition = 'none';
                    }, 500);
                });
                
                btnNext.addEventListener('click', () => {
                    let targetPos = currentPos + 400;
                    if (targetPos >= track.scrollWidth / 3) targetPos -= track.scrollWidth / 3;
                    
                    track.style.transition = 'transform 0.5s ease-out';
                    track.style.transform = `translate3d(-${targetPos}px, 0, 0)`;
                    currentPos = targetPos;
                    
                    setTimeout(() => {
                        track.style.transition = 'none';
                    }, 500);
                });
            }
        }
    });
    </script>
"""

    content = "".join(sections)
    
    # insert script right before </body>
    if "</body>" in content:
        content = content.replace("</body>", js_script + "\n</body>")
    else:
        content += js_script
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced section and added scripts.")
else:
    print("Error: Target section not found.")
