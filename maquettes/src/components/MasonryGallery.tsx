import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X } from "lucide-react";
import { GALLERY, GalleryImage } from "@/data/gallery";

const spanClasses: Record<GalleryImage["span"], string> = {
  hero: "md:col-span-8 md:row-span-2 aspect-[16/10]",
  tall: "md:col-span-4 md:row-span-2 aspect-[3/4]",
  wide: "md:col-span-8 aspect-[16/9]",
  square: "md:col-span-4 aspect-square",
};

export default function MasonryGallery() {
  const [active, setActive] = useState<GalleryImage | null>(null);

  return (
    <section
      data-testid="gallery-section"
      className="py-24 md:py-32 bg-base"
      id="gallery"
    >
      <div className="container-luxe">
        <div className="mb-14 flex flex-col md:flex-row md:items-end justify-between gap-6">
          <div>
            <p className="eyebrow">Espace Photo</p>
            <h2 className="mt-3 font-display text-4xl sm:text-5xl tracking-tight">
              L'instant suspendu.
            </h2>
          </div>
          <p className="text-muted-app max-w-md">
            Salle, dressage, mains et matière. La vie au passage chez{" "}
            <span className="italic">Maison Lumière</span>.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-12 gap-4 md:gap-5 auto-rows-[160px]">
          {GALLERY.map((img, idx) => (
            <motion.button
              key={img.id}
              data-testid={`gallery-item-${img.id}`}
              onClick={() => setActive(img)}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-80px" }}
              transition={{ duration: 0.6, delay: idx * 0.06 }}
              className={`relative overflow-hidden rounded-md group ${spanClasses[img.span]}`}
            >
              <img
                src={img.src}
                alt={img.alt}
                className="img-luxe w-full h-full object-cover transition-transform duration-[1200ms] ease-out group-hover:scale-[1.06]"
                loading="lazy"
              />
              <div className="absolute inset-0 bg-black/0 group-hover:bg-black/15 transition-colors duration-500" />
            </motion.button>
          ))}
        </div>
      </div>

      <AnimatePresence>
        {active && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            data-testid="gallery-lightbox"
            className="fixed inset-0 z-[60] bg-black/90 flex items-center justify-center p-4"
            onClick={() => setActive(null)}
          >
            <button
              className="absolute top-6 right-6 text-white/80 hover:text-white p-2"
              onClick={() => setActive(null)}
              aria-label="Close"
              data-testid="gallery-lightbox-close"
            >
              <X className="h-6 w-6" />
            </button>
            <motion.img
              initial={{ scale: 0.95, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.97, opacity: 0 }}
              transition={{ duration: 0.4 }}
              src={active.src}
              alt={active.alt}
              className="max-h-[90vh] max-w-[90vw] object-contain rounded-md"
              onClick={(e) => e.stopPropagation()}
            />
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
