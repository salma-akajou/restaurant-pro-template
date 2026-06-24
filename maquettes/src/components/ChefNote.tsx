import { motion } from "framer-motion";

export default function ChefNote() {
  return (
    <section
      data-testid="chef-section"
      className="py-24 md:py-32 bg-surface border-y border-subtle"
    >
      <div className="container-luxe grid md:grid-cols-12 gap-12 md:gap-20 items-center">
        <motion.div
          initial={{ opacity: 0, x: -30 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="md:col-span-5"
        >
          <div className="relative aspect-[3/4] overflow-hidden rounded-md">
            <img
              src="https://images.unsplash.com/photo-1663530761401-15eefb544889?w=1200&q=85"
              alt="Chef Hugo Marais"
              className="img-luxe w-full h-full object-cover"
              loading="lazy"
            />
          </div>
          <p className="mt-5 text-xs text-soft-app tracking-widest uppercase">
            Chef Hugo Marais · Étoilé
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, x: 30 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.1 }}
          className="md:col-span-7"
        >
          <p className="eyebrow">Le mot du chef</p>
          <blockquote className="mt-5 font-display text-3xl sm:text-4xl leading-tight tracking-tight text-primary-app">
            « Cuisiner, ce n'est pas plier la matière à sa volonté.
            <span className="italic accent-color">
              {" "}
              C'est l'écouter, l'apprivoiser, lui rendre sa lumière.
            </span>{" "}
            Voilà la promesse de cette maison. »
          </blockquote>
          <div className="mt-8 flex items-center gap-4">
            <span className="text-sm text-muted-app">— Hugo Marais</span>
            <span className="h-px w-12 bg-strong" />
            <span className="text-xs text-soft-app uppercase tracking-widest">
              15 ans d'obsession
            </span>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
