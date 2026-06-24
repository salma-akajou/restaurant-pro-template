import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import { ArrowRight, Star } from "lucide-react";
import { BRAND } from "@/data/brand";

const HERO_VIDEO =
  "https://videos.pexels.com/video-files/3195394/3195394-uhd_2560_1440_25fps.mp4";
const HERO_FALLBACK =
  "https://images.pexels.com/photos/10633476/pexels-photo-10633476.jpeg?w=1920";

export default function Hero() {
  return (
    <section
      data-testid="hero-section"
      className="relative h-[92vh] min-h-[640px] w-full overflow-hidden flex items-end"
    >
      {/* Video background */}
      <div className="absolute inset-0">
        <video
          autoPlay
          muted
          loop
          playsInline
          poster={HERO_FALLBACK}
          className="absolute inset-0 w-full h-full object-cover"
          data-testid="hero-video"
        >
          <source src={HERO_VIDEO} type="video/mp4" />
        </video>
        <div
          className="absolute inset-0"
          style={{
            background:
              "linear-gradient(180deg, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.1) 40%, rgba(0,0,0,0.7) 100%)",
          }}
        />
      </div>

      <div className="relative z-10 container-luxe pb-20 md:pb-28 text-white">
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.7 }}
          className="text-xs tracking-[0.32em] uppercase mb-6 text-white/80"
        >
          Casablanca · Depuis 2014 · ★ ★ ★ ★ ★
        </motion.p>

        <motion.h1
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.35, duration: 0.8, ease: [0.2, 0.8, 0.2, 1] }}
          className="font-display text-5xl sm:text-7xl lg:text-8xl leading-[0.95] tracking-tight max-w-4xl"
        >
          {BRAND.name.split(" ")[0]}
          <br />
          <span className="italic font-light">{BRAND.name.split(" ")[1]}</span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.55, duration: 0.7 }}
          className="mt-6 max-w-xl text-base sm:text-lg text-white/85 leading-relaxed"
        >
          {BRAND.tagline}. Une cuisine d'auteur, des produits vivants, un
          service qui sait se faire oublier.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.75, duration: 0.7 }}
          className="mt-10 flex flex-wrap gap-4"
        >
          <Link
            to="/menu"
            data-testid="hero-cta-menu"
            className="group inline-flex items-center gap-3 px-7 py-4 rounded-full bg-white text-black text-sm tracking-wide hover-lift"
          >
            Explorer le menu
            <ArrowRight className="h-4 w-4 group-hover:translate-x-1 transition-transform" />
          </Link>
          <a
            href={`https://wa.me/${BRAND.whatsapp.replace(/[^\d]/g, "")}`}
            target="_blank"
            rel="noopener noreferrer"
            data-testid="hero-cta-reserve"
            className="inline-flex items-center gap-3 px-7 py-4 rounded-full border border-white/30 text-white text-sm tracking-wide hover:bg-white/10 transition-colors"
          >
            Réserver une table
          </a>
        </motion.div>

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.1, duration: 0.7 }}
          className="mt-14 flex items-center gap-6 text-white/70 text-xs tracking-wider"
        >
          <div className="flex items-center gap-1.5">
            {[...Array(5)].map((_, i) => (
              <Star key={i} className="h-3 w-3 fill-current" />
            ))}
            <span className="ml-2">4.9 · 1 248 avis</span>
          </div>
          <span className="hidden sm:block">·</span>
          <span className="hidden sm:block">Guide Michelin 2024</span>
        </motion.div>
      </div>

      {/* Scroll indicator */}
      <motion.div
        animate={{ y: [0, 8, 0] }}
        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
        className="absolute bottom-6 left-1/2 -translate-x-1/2 z-10 text-white/60 text-[10px] tracking-[0.3em] uppercase"
      >
        ↓ scroll
      </motion.div>
    </section>
  );
}
