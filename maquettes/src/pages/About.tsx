import { motion } from "framer-motion";
import PageTransition from "@/components/PageTransition";
import { BRAND } from "@/data/brand";
import { MapPin, Mail, Phone } from "lucide-react";

const TIMELINE = [
  {
    year: "2014",
    title: "L'ouverture",
    desc: "Hugo Marais ouvre Maison Lumière au cœur de Casablanca, après huit ans en cuisines étoilées parisiennes.",
  },
  {
    year: "2017",
    title: "Première étoile",
    desc: "Reconnaissance du Guide Michelin pour une cuisine 'd'une précision rare'.",
  },
  {
    year: "2021",
    title: "La Bibliothèque",
    desc: "Ouverture du salon privé La Bibliothèque, lieu d'événements littéraires et culinaires.",
  },
  {
    year: "2025",
    title: "10 ans",
    desc: "Une décennie d'obsessions, 600 producteurs partenaires, 14 menus saisonniers.",
  },
];

export default function About() {
  return (
    <PageTransition>
      <section className="relative h-[60vh] min-h-[400px] overflow-hidden flex items-end">
        <img
          src="https://images.pexels.com/photos/10633476/pexels-photo-10633476.jpeg?w=1920"
          alt="Maison Lumière"
          className="absolute inset-0 w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-black/55" />
        <div className="relative z-10 container-luxe pb-16 text-white">
          <p className="text-xs tracking-[0.32em] uppercase mb-4 text-white/80">
            La Maison
          </p>
          <h1 className="font-display text-6xl sm:text-7xl tracking-tight">
            Notre histoire
          </h1>
        </div>
      </section>

      {/* Our story */}
      <section className="py-24 md:py-32 bg-base">
        <div className="container-luxe grid md:grid-cols-12 gap-12">
          <div className="md:col-span-5">
            <p className="eyebrow">Manifeste</p>
            <h2 className="mt-3 font-display text-4xl sm:text-5xl tracking-tight leading-tight">
              Une cuisine
              <br />
              <span className="italic accent-color">de la lumière.</span>
            </h2>
          </div>
          <div className="md:col-span-7 space-y-5 text-lg leading-relaxed text-muted-app">
            <p>
              <span className="text-primary-app font-medium">
                Maison Lumière
              </span>{" "}
              est née d'une obsession simple : rendre la lumière aux produits.
              Pas de fumée, pas d'artifice. La cuisson juste, le geste pensé, le
              service discret.
            </p>
            <p>
              Chaque saison, le chef Hugo Marais redessine une carte courte,
              presque chuchotée, qui suit le rythme des maraîchers, des pêcheurs
              et des éleveurs de la région. Le menu change quatre fois par an —
              parfois davantage.
            </p>
            <p>
              Cette maison croit qu'un dîner peut être une parenthèse précieuse.
              Un moment où le temps ralentit, où la conversation s'épanouit,
              où le souvenir s'imprime durablement.
            </p>
          </div>
        </div>
      </section>

      {/* Timeline */}
      <section className="py-24 md:py-32 bg-surface border-y border-subtle">
        <div className="container-luxe">
          <p className="eyebrow text-center">Chronologie</p>
          <h2 className="mt-3 font-display text-4xl sm:text-5xl text-center mb-20">
            10 ans, <span className="italic accent-color">14 menus</span>.
          </h2>

          <div className="relative">
            <div className="absolute left-1/2 -translate-x-px top-0 bottom-0 w-px bg-strong hidden md:block" />
            <div className="space-y-12 md:space-y-20">
              {TIMELINE.map((t, idx) => (
                <motion.div
                  key={t.year}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: idx * 0.1 }}
                  className={`grid md:grid-cols-2 gap-6 items-center ${
                    idx % 2 === 0 ? "" : "md:[direction:rtl]"
                  }`}
                >
                  <div
                    className={`md:[direction:ltr] ${
                      idx % 2 === 0 ? "md:text-right md:pr-16" : "md:pl-16"
                    }`}
                  >
                    <p
                      className="font-display text-6xl accent-color"
                      style={{ color: "var(--color-accent)" }}
                    >
                      {t.year}
                    </p>
                    <h3 className="font-display text-2xl mt-2">{t.title}</h3>
                  </div>
                  <p
                    className={`md:[direction:ltr] text-muted-app leading-relaxed ${
                      idx % 2 === 0 ? "md:pl-16" : "md:pr-16 md:text-right"
                    }`}
                  >
                    {t.desc}
                  </p>
                </motion.div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Contact + Map */}
      <section className="py-24 md:py-32 bg-base">
        <div className="container-luxe grid md:grid-cols-2 gap-12">
          <div>
            <p className="eyebrow">Nous rendre visite</p>
            <h2 className="mt-3 font-display text-4xl sm:text-5xl">Contact</h2>
            <ul className="mt-10 space-y-5 text-muted-app">
              <li className="flex gap-3">
                <MapPin className="h-5 w-5 mt-0.5 accent-color shrink-0" />
                <span>{BRAND.address}</span>
              </li>
              <li className="flex gap-3">
                <Phone className="h-5 w-5 accent-color shrink-0" />
                <span>{BRAND.phone}</span>
              </li>
              <li className="flex gap-3">
                <Mail className="h-5 w-5 accent-color shrink-0" />
                <span>{BRAND.email}</span>
              </li>
            </ul>
            <p className="mt-10 text-sm text-soft-app leading-relaxed">
              Mardi — Samedi · Service 12h-14h & 19h30-22h30
              <br />
              Fermé Dimanche & Lundi
            </p>
          </div>
          <div className="aspect-[4/3] rounded-md overflow-hidden border border-subtle bg-elevated grid place-items-center text-soft-app">
            <iframe
              title="map"
              src="https://maps.google.com/maps?q=Casablanca&t=&z=13&ie=UTF8&iwloc=&output=embed"
              className="w-full h-full grayscale opacity-90"
              loading="lazy"
            />
          </div>
        </div>
      </section>

      {/* Legal */}
      <section
        id="legal"
        className="py-24 md:py-32 bg-surface border-t border-subtle"
      >
        <div className="container-luxe max-w-4xl">
          <p className="eyebrow">Mentions légales</p>
          <h2 className="mt-3 font-display text-4xl sm:text-5xl mb-12">
            Conditions
          </h2>

          <div className="space-y-12 text-muted-app leading-relaxed">
            <article>
              <h3 className="font-display text-2xl text-primary-app mb-4">
                Conditions Générales de Vente
              </h3>
              <p>
                Les présentes conditions régissent les commandes passées via le
                site, le service WhatsApp et nos partenaires de livraison
                (Glovo, Talabat). Toute commande implique l'acceptation pleine
                et entière des présentes conditions.
              </p>
            </article>
            <article>
              <h3 className="font-display text-2xl text-primary-app mb-4">
                Livraison
              </h3>
              <p>
                Les livraisons sont assurées par nos partenaires dans un rayon
                de 7 km autour de Casablanca centre. Les délais moyens
                constatés sont de 35 à 60 minutes selon la zone et l'affluence.
              </p>
            </article>
            <article>
              <h3 className="font-display text-2xl text-primary-app mb-4">
                Confidentialité
              </h3>
              <p>
                Vos données personnelles sont traitées avec le plus grand soin
                et ne sont jamais cédées à des tiers à des fins commerciales.
                Conformément à la loi 09-08, vous disposez d'un droit d'accès,
                de rectification et d'opposition.
              </p>
            </article>
            <article>
              <h3 className="font-display text-2xl text-primary-app mb-4">
                Allergènes & Conformité
              </h3>
              <p>
                Les allergènes majeurs sont signalés sur chaque plat. En cas
                d'allergie sévère, merci de prévenir le service en amont de
                votre commande. La cuisine traite des produits laitiers, du
                gluten, des fruits à coque et des fruits de mer.
              </p>
            </article>
          </div>
        </div>
      </section>
    </PageTransition>
  );
}
