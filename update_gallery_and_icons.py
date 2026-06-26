import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\about.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Remove the old script section
content = re.sub(r'<!-- Editorial Gallery JS -->.*?</script>\s*', '', content, flags=re.DOTALL)

# Locate the Sections to replace
# We need to replace from <section class="py-24 md:py-32 bg-[#050505] overflow-hidden relative border-t border-white/5" id="editorial-gallery">
# to the end of the <section class="py-24 md:py-32 bg-[#0a0a0a] relative overflow-hidden"> which is the community section.

start_gallery = '<!-- ================= EDITORIAL GALLERY SECTION ================= -->'
end_community = '</section>\n\n    <!-- ================= INFO SECTION ================= -->'
# or let's use regex to find the block
match = re.search(r'(<!-- ================= EDITORIAL GALLERY SECTION ================= -->.*?</section>\s*<!-- ================= COMMUNITY SECTION ================= -->.*?</section>)', content, re.DOTALL)

new_sections = """<!-- ================= EDITORIAL GALLERY SECTION ================= -->
    <section class="py-24 md:py-32 bg-[#050505] overflow-hidden relative border-t border-white/5" id="editorial-gallery">
        <!-- Glow effect -->
        <div class="absolute left-1/2 top-0 -translate-x-1/2 w-[800px] h-[400px] bg-primary/5 blur-[120px] rounded-full pointer-events-none z-0"></div>
        
        <div class="w-full max-w-7xl mx-auto px-4 relative z-10">
            <div class="flex flex-col md:flex-row justify-between items-end mb-12">
                <div class="text-left fade-up">
                    <p class="text-[10px] md:text-xs text-primary tracking-[0.2em] uppercase font-bold mb-4" data-i18n="about-soul-eyebrow">Editorial Gallery</p>
                    <h2 class="font-serif text-3xl md:text-4xl lg:text-5xl text-white mb-4" data-i18n="about-soul-title">L'âme de Maison Lumière</h2>
                    <div class="flex items-center gap-2 opacity-80">
                        <div class="h-px w-6 bg-primary"></div>
                        <div class="w-1 h-1 rotate-45 bg-primary"></div>
                        <div class="h-px w-6 bg-primary"></div>
                    </div>
                </div>
                <div class="flex gap-3 fade-up mt-6 md:mt-0">
                    <button onclick="scrollGallery('left')" class="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center hover:bg-white/10 hover:border-white transition-all text-white/70 hover:text-white backdrop-blur-sm z-50">
                        <i data-lucide="chevron-left" class="w-5 h-5"></i>
                    </button>
                    <button onclick="scrollGallery('right')" class="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center hover:bg-white/10 hover:border-white transition-all text-white/70 hover:text-white backdrop-blur-sm z-50">
                        <i data-lucide="chevron-right" class="w-5 h-5"></i>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Gallery Container -->
        <div class="relative w-full group mt-4 z-10" id="gallery-wrapper">
            <!-- Track -->
            <div id="gallery-track" class="flex items-center h-[320px] md:h-[450px] gap-4 md:gap-6 px-4 md:px-[calc((100vw-1280px)/2+16px)] w-full overflow-x-auto snap-x snap-mandatory scrollbar-hide pb-8">
                <!-- Items -->
                <div class="w-[180px] md:w-[240px] h-[240px] md:h-[320px] rounded-[20px] overflow-hidden shrink-0 relative snap-center transform md:-translate-y-6 shadow-[0_15px_30px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=600&q=80" alt="Ambiance" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="w-[220px] md:w-[300px] h-[280px] md:h-[380px] rounded-[20px] overflow-hidden shrink-0 relative snap-center transform md:translate-y-4 shadow-[0_15px_30px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=800&q=80" alt="Cocktail" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="w-[160px] md:w-[220px] h-[220px] md:h-[300px] rounded-[20px] overflow-hidden shrink-0 relative snap-center transform md:-translate-y-10 shadow-[0_15px_30px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=500&q=80" alt="Planche" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="w-[200px] md:w-[280px] h-[260px] md:h-[360px] rounded-[20px] overflow-hidden shrink-0 relative snap-center transform md:translate-y-6 shadow-[0_15px_30px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=700&q=80" alt="Plat Signature" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="w-[180px] md:w-[240px] h-[240px] md:h-[320px] rounded-[20px] overflow-hidden shrink-0 relative snap-center transform md:-translate-y-4 shadow-[0_15px_30px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=600&q=80" alt="Dessert" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                <div class="w-[240px] md:w-[320px] h-[300px] md:h-[400px] rounded-[20px] overflow-hidden shrink-0 relative snap-center transform md:translate-y-8 shadow-[0_15px_30px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-700 ease-out hover:scale-[1.08] hover:z-20 hover:shadow-[0_30px_50px_rgba(193,165,141,0.2)] group/card">
                    <div class="absolute inset-0 bg-black/20 group-hover/card:bg-black/0 transition-colors duration-700 z-10 pointer-events-none"></div>
                    <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=800&q=80" alt="Restaurant Interieur" class="w-full h-full object-cover saturate-[0.6] contrast-125 group-hover/card:saturate-100 transition-all duration-700">
                </div>
                
                 <!-- Spacer to allow scrolling past last item cleanly -->
                 <div class="w-4 md:w-8 shrink-0"></div>
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
                    <!-- Real Instagram Logo -->
                    <svg class="w-10 h-10 mb-6 transition-transform duration-500 group-hover:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <defs>
                            <linearGradient id="ig-grad" x1="0%" y1="100%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#fd5949" />
                                <stop offset="50%" stop-color="#d6249f" />
                                <stop offset="100%" stop-color="#285AEB" />
                            </linearGradient>
                        </defs>
                        <rect x="2" y="2" width="20" height="20" rx="5" ry="5" stroke="url(#ig-grad)"></rect>
                        <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" stroke="url(#ig-grad)"></path>
                        <line x1="17.5" y1="6.5" x2="17.51" y2="6.5" stroke="url(#ig-grad)"></line>
                    </svg>
                    <h3 class="text-xs text-gray-400 tracking-[0.2em] uppercase mb-2">Instagram</h3>
                    <div class="font-serif text-3xl md:text-4xl text-white mb-2 transition-all duration-700 group-hover:brightness-125">42.8K</div>
                    <div class="text-[10px] text-[#C1A58D] mb-8 tracking-widest">+12% CE MOIS</div>
                    <a href="#" class="px-6 py-2 rounded-full border border-white/20 text-xs text-white/80 hover:text-white hover:border-primary hover:bg-primary/10 transition-colors duration-300 z-10">Visiter</a>
                </div>

                <!-- Facebook -->
                <div class="group flex flex-col items-center justify-center p-10 rounded-[24px] bg-[#050505] border border-[#C1A58D]/20 shadow-lg hover:-translate-y-2 hover:shadow-[0_0_30px_rgba(193,165,141,0.15)] transition-all duration-700 ease-out relative overflow-hidden fade-up" style="transition-delay: 100ms">
                    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>
                    <!-- Real Facebook Logo -->
                    <svg class="w-10 h-10 mb-6 transition-transform duration-500 group-hover:scale-110" viewBox="0 0 24 24" fill="#1877F2">
                        <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                    </svg>
                    <h3 class="text-xs text-gray-400 tracking-[0.2em] uppercase mb-2">Facebook</h3>
                    <div class="font-serif text-3xl md:text-4xl text-white mb-2 transition-all duration-700 group-hover:brightness-125">18.4K</div>
                    <div class="text-[10px] text-[#C1A58D] mb-8 tracking-widest">+5% CE MOIS</div>
                    <a href="#" class="px-6 py-2 rounded-full border border-white/20 text-xs text-white/80 hover:text-white hover:border-primary hover:bg-primary/10 transition-colors duration-300 z-10">Visiter</a>
                </div>

                <!-- TikTok -->
                <div class="group flex flex-col items-center justify-center p-10 rounded-[24px] bg-[#050505] border border-[#C1A58D]/20 shadow-lg hover:-translate-y-2 hover:shadow-[0_0_30px_rgba(193,165,141,0.15)] transition-all duration-700 ease-out relative overflow-hidden fade-up" style="transition-delay: 200ms">
                    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>
                    <!-- Real TikTok Logo -->
                    <svg class="w-10 h-10 mb-6 transition-transform duration-500 group-hover:scale-110" viewBox="0 0 24 24" fill="white">
                        <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z" style="filter: drop-shadow(2px 2px 0px #ff0050) drop-shadow(-2px -2px 0px #00f2fe);"/>
                    </svg>
                    <h3 class="text-xs text-gray-400 tracking-[0.2em] uppercase mb-2">TikTok</h3>
                    <div class="font-serif text-3xl md:text-4xl text-white mb-2 transition-all duration-700 group-hover:brightness-125">95.2K</div>
                    <div class="text-[10px] text-[#C1A58D] mb-8 tracking-widest">+28% CE MOIS</div>
                    <a href="#" class="px-6 py-2 rounded-full border border-white/20 text-xs text-white/80 hover:text-white hover:border-primary hover:bg-primary/10 transition-colors duration-300 z-10">Visiter</a>
                </div>

                <!-- TripAdvisor -->
                <div class="group flex flex-col items-center justify-center p-10 rounded-[24px] bg-[#050505] border border-[#C1A58D]/20 shadow-lg hover:-translate-y-2 hover:shadow-[0_0_30px_rgba(193,165,141,0.15)] transition-all duration-700 ease-out relative overflow-hidden fade-up" style="transition-delay: 300ms">
                    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>
                    <!-- Real TripAdvisor Logo (simplified) -->
                    <svg class="w-10 h-10 mb-6 transition-transform duration-500 group-hover:scale-110" viewBox="0 0 24 24" fill="#34e0a1">
                        <path d="M23.16 11.23c-1.34-1.28-3.08-1.9-4.88-1.85-2.02.04-3.95.84-5.46 2.19l-.82.72-.82-.72c-1.51-1.35-3.44-2.15-5.46-2.19-1.8-.05-3.54.57-4.88 1.85a7.355 7.355 0 0 0-2.08 5.61c.27 2.11 1.48 3.99 3.25 5.09.47.29 1.05.15 1.34-.32.29-.47.15-1.05-.32-1.34-1.3-.8-2.18-2.18-2.38-3.72a5.412 5.412 0 0 1 1.54-4.14c1.03-1 2.37-1.46 3.75-1.42 1.49.03 2.91.64 4 1.63L11.02 14c-.01.01-.03.02-.04.04l-.06.07-.06.07c-.4.5-.32 1.23.18 1.63s1.23.32 1.63-.18l.06-.07.06-.07.04-.04c.03-.04.05-.08.08-.12l2.36-2.08c1.09-.99 2.51-1.6 4-1.63 1.38-.04 2.72.42 3.75 1.42 1.01.99 1.56 2.41 1.54 3.86-.02 1.48-.64 2.87-1.73 3.83-.41.36-1.12.87-1.78.87-.2 0-.41-.05-.6-.16-.47-.27-1.07-.12-1.34.35-.27.47-.12 1.07.35 1.34.38.22.81.33 1.25.33 1.13 0 2.22-.84 2.81-1.36 1.43-1.25 2.25-3.08 2.28-5.02.04-1.92-.66-3.79-1.98-5.05zm-16.71 7.21c-1.54 0-2.8-1.25-2.8-2.8 0-1.54 1.25-2.8 2.8-2.8 1.54 0 2.8 1.25 2.8 2.8 0 1.54-1.25 2.8-2.8 2.8zm11.1 0c-1.54 0-2.8-1.25-2.8-2.8 0-1.54 1.25-2.8 2.8-2.8 1.54 0 2.8 1.25 2.8 2.8 0 1.54-1.25 2.8-2.8 2.8z"/>
                    </svg>
                    <h3 class="text-xs text-gray-400 tracking-[0.2em] uppercase mb-2">TripAdvisor</h3>
                    <div class="font-serif text-3xl md:text-4xl text-white mb-2 transition-all duration-700 group-hover:brightness-125">4.9<span class="text-primary text-2xl ml-1">★</span></div>
                    <div class="text-[10px] text-gray-400 mb-8 tracking-widest uppercase">3 400 avis</div>
                    <a href="#" class="px-6 py-2 rounded-full border border-white/20 text-xs text-white/80 hover:text-white hover:border-primary hover:bg-primary/10 transition-colors duration-300 z-10">Visiter</a>
                </div>
            </div>
        </div>
    </section>"""

if match:
    content = content[:match.start()] + new_sections + content[match.end():]
    
    js_script = """
    <!-- Editorial Gallery JS -->
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        // Gallery Auto-Scroll (Stop and Go)
        const track = document.getElementById('gallery-track');
        let autoScrollInterval;

        function startAutoScroll() {
            autoScrollInterval = setInterval(() => {
                if (track) {
                    const firstItem = track.querySelector('.group\\\\/card');
                    if(firstItem) {
                        const itemWidth = firstItem.offsetWidth + 24; // approx gap
                        
                        // check if end is reached
                        if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 10) {
                            track.scrollTo({ left: 0, behavior: 'smooth' });
                        } else {
                            track.scrollBy({ left: itemWidth, behavior: 'smooth' });
                        }
                    }
                }
            }, 3000); 
        }

        function stopAutoScroll() {
            clearInterval(autoScrollInterval);
        }

        if (track) {
            startAutoScroll();
            track.addEventListener('mouseenter', stopAutoScroll);
            track.addEventListener('mouseleave', startAutoScroll);
            track.addEventListener('touchstart', stopAutoScroll);
            track.addEventListener('touchend', startAutoScroll);
        }
    });

    function scrollGallery(direction) {
        const track = document.getElementById('gallery-track');
        if (track) {
            const firstItem = track.querySelector('.group\\\\/card');
            if(firstItem) {
                const itemWidth = firstItem.offsetWidth + 24;
                if (direction === 'left') {
                    track.scrollBy({ left: -itemWidth, behavior: 'smooth' });
                } else {
                    track.scrollBy({ left: itemWidth, behavior: 'smooth' });
                }
            }
        }
    }
    </script>
"""
    if "</body>" in content:
        content = content.replace("</body>", js_script + "\n</body>")
    else:
        content += js_script
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced sections successfully with new changes.")
else:
    print("Could not match the block.")
