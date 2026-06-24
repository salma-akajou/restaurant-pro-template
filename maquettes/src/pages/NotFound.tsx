import { Link } from "react-router-dom";
import PageTransition from "@/components/PageTransition";

export default function NotFound() {
  return (
    <PageTransition>
      <section className="min-h-[70vh] grid place-items-center text-center px-6">
        <div className="max-w-md">
          <p className="eyebrow">404</p>
          <h1 className="mt-4 font-display text-6xl">Page introuvable.</h1>
          <p className="mt-4 text-muted-app">
            Cette page s'est égarée entre deux services. Retrouvons le chemin.
          </p>
          <Link
            to="/"
            data-testid="back-home"
            className="mt-8 inline-block px-6 py-3 rounded-full bg-primary-brand text-sm tracking-wide hover-lift"
            style={{ color: "var(--bg-surface)" }}
          >
            Retour à l'accueil
          </Link>
        </div>
      </section>
    </PageTransition>
  );
}
