import { Link } from "react-router-dom";
import { Instagram, Facebook, MapPin, Mail, Phone } from "lucide-react";
import { BRAND } from "@/data/brand";

export default function Footer() {
  return (
    <footer
      data-testid="site-footer"
      className="mt-32 border-t border-subtle bg-surface"
    >
      <div className="container-luxe py-20">
        <div className="grid md:grid-cols-4 gap-12">
          <div className="md:col-span-2">
            <h3 className="font-display text-3xl mb-3">
              {BRAND.name.split(" ")[0]}
              <span className="italic accent-color">
                {" "}
                {BRAND.name.split(" ")[1]}
              </span>
            </h3>
            <p className="text-muted-app max-w-md leading-relaxed">
              {BRAND.tagline}. Une expérience gastronomique pensée comme une
              parenthèse hors du temps.
            </p>
          </div>

          <div>
            <p className="eyebrow mb-5">Navigation</p>
            <ul className="space-y-3 text-sm">
              <li>
                <Link
                  to="/menu"
                  className="text-muted-app hover:text-primary-app transition-colors"
                >
                  Le Menu
                </Link>
              </li>
              <li>
                <Link
                  to="/bibliotheque"
                  className="text-muted-app hover:text-primary-app transition-colors"
                >
                  Bibliothèque
                </Link>
              </li>
              <li>
                <Link
                  to="/about"
                  className="text-muted-app hover:text-primary-app transition-colors"
                >
                  À propos
                </Link>
              </li>
              <li>
                <Link
                  to="/about#legal"
                  className="text-muted-app hover:text-primary-app transition-colors"
                >
                  Conditions de Vente
                </Link>
              </li>
            </ul>
          </div>

          <div>
            <p className="eyebrow mb-5">Contact</p>
            <ul className="space-y-3 text-sm text-muted-app">
              <li className="flex items-start gap-2">
                <MapPin className="h-4 w-4 mt-0.5 shrink-0" />
                {BRAND.address}
              </li>
              <li className="flex items-center gap-2">
                <Phone className="h-4 w-4 shrink-0" />
                {BRAND.phone}
              </li>
              <li className="flex items-center gap-2">
                <Mail className="h-4 w-4 shrink-0" />
                {BRAND.email}
              </li>
              <li className="flex items-center gap-4 pt-2">
                <a
                  href={BRAND.social.instagram}
                  className="hover:text-primary-app"
                  aria-label="Instagram"
                >
                  <Instagram className="h-4 w-4" />
                </a>
                <a
                  href={BRAND.social.facebook}
                  className="hover:text-primary-app"
                  aria-label="Facebook"
                >
                  <Facebook className="h-4 w-4" />
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="divider-luxe my-12" />

        <div className="flex flex-col md:flex-row justify-between gap-4 text-xs text-soft-app">
          <p>
            © {new Date().getFullYear()} {BRAND.name}. Tous droits réservés.
          </p>
          <p className="tracking-[0.2em] uppercase">
            RestoFlex Core — White-Label Hospitality Template
          </p>
        </div>
      </div>
    </footer>
  );
}
