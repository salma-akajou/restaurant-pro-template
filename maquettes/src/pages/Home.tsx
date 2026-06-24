import PageTransition from "@/components/PageTransition";
import Hero from "@/components/Hero";
import MasonryGallery from "@/components/MasonryGallery";
import Reviews from "@/components/Reviews";
import SignatureDishes from "@/components/SignatureDishes";
import ChefNote from "@/components/ChefNote";
import { Link } from "react-router-dom";
import { ArrowRight } from "lucide-react";

export default function Home() {
  return (
    <PageTransition>
      <Hero />
      <SignatureDishes />
      <MasonryGallery />
      <ChefNote />
      <Reviews />

      {/* Final CTA */}
      <section
        data-testid="footer-cta"
        className="py-28 md:py-40 bg-base text-center"
      >
        <div className="container-luxe max-w-3xl">
          <p className="eyebrow">Réservation</p>
          <h2 className="mt-5 font-display text-5xl sm:text-6xl tracking-tight">
            Une table.
            <br />
            <span className="italic accent-color">Un soir à part.</span>
          </h2>
          <p className="mt-6 text-muted-app text-lg leading-relaxed">
            Réservez en deux clics — ou commandez directement votre menu favori
            via WhatsApp.
          </p>
          <div className="mt-10 flex flex-wrap justify-center gap-4">
            <Link
              to="/menu"
              data-testid="cta-menu-bottom"
              className="group inline-flex items-center gap-3 px-7 py-4 rounded-full bg-primary-brand text-sm tracking-wide hover-lift"
              style={{ color: "var(--bg-surface)" }}
            >
              Voir la carte
              <ArrowRight className="h-4 w-4 group-hover:translate-x-1 transition-transform" />
            </Link>
            <Link
              to="/about"
              className="inline-flex items-center gap-3 px-7 py-4 rounded-full border border-strong text-sm tracking-wide hover:bg-surface transition-colors"
            >
              Notre histoire
            </Link>
          </div>
        </div>
      </section>
    </PageTransition>
  );
}
