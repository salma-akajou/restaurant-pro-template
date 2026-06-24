import { useRef } from "react";
import { motion } from "framer-motion";
import { Star, ChevronLeft, ChevronRight } from "lucide-react";
import { REVIEWS } from "@/data/reviews";

export default function Reviews() {
  const scrollerRef = useRef<HTMLDivElement>(null);

  const scroll = (dir: "left" | "right") => {
    const el = scrollerRef.current;
    if (!el) return;
    const amount = el.clientWidth * 0.8;
    el.scrollBy({
      left: dir === "left" ? -amount : amount,
      behavior: "smooth",
    });
  };

  return (
    <section
      data-testid="reviews-section"
      className="py-24 md:py-32 bg-surface border-y border-subtle"
    >
      <div className="container-luxe">
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
          <div>
            <p className="eyebrow">Ce qu'ils en disent</p>
            <h2 className="mt-3 font-display text-4xl sm:text-5xl">
              4.9 sur Google.
              <br />
              <span className="italic accent-color">
                1 248 voix singulières.
              </span>
            </h2>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={() => scroll("left")}
              data-testid="reviews-prev"
              className="p-3 rounded-full border border-subtle hover:border-strong hover:bg-base transition-colors"
              aria-label="Previous reviews"
            >
              <ChevronLeft className="h-4 w-4" />
            </button>
            <button
              onClick={() => scroll("right")}
              data-testid="reviews-next"
              className="p-3 rounded-full border border-subtle hover:border-strong hover:bg-base transition-colors"
              aria-label="Next reviews"
            >
              <ChevronRight className="h-4 w-4" />
            </button>
          </div>
        </div>

        <div
          ref={scrollerRef}
          className="flex gap-5 overflow-x-auto hide-scrollbar pb-4 snap-x snap-mandatory"
        >
          {REVIEWS.map((r, idx) => (
            <motion.article
              key={r.id}
              data-testid={`review-${r.id}`}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.55, delay: idx * 0.07 }}
              className="snap-start shrink-0 w-[320px] md:w-[380px] bg-elevated border border-subtle rounded-2xl p-7 flex flex-col gap-4"
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div
                    className="w-10 h-10 rounded-full grid place-items-center text-sm font-medium"
                    style={{
                      backgroundColor: "var(--color-accent)",
                      color: "var(--bg-surface)",
                    }}
                  >
                    {r.initials}
                  </div>
                  <div>
                    <p className="text-sm font-medium text-primary-app leading-tight">
                      {r.author}
                    </p>
                    <p className="text-[11px] text-soft-app">{r.date}</p>
                  </div>
                </div>
                <span className="text-[10px] uppercase tracking-wider text-soft-app">
                  {r.source}
                </span>
              </div>

              <div className="flex items-center gap-0.5 accent-color">
                {[...Array(r.rating)].map((_, i) => (
                  <Star key={i} className="h-3.5 w-3.5 fill-current" />
                ))}
              </div>

              <p className="text-muted-app leading-relaxed flex-1">
                "{r.quote}"
              </p>
            </motion.article>
          ))}
        </div>
      </div>
    </section>
  );
}
