import { useState, useMemo } from "react";
import { motion } from "framer-motion";
import PageTransition from "@/components/PageTransition";
import { BLOG_POSTS, BLOG_CATEGORIES, BlogPost } from "@/data/blog";
import { ArrowRight } from "lucide-react";

type Filter = "Tous" | BlogPost["category"];

export default function Blog() {
  const [filter, setFilter] = useState<Filter>("Tous");

  const filtered = useMemo(
    () =>
      filter === "Tous"
        ? BLOG_POSTS
        : BLOG_POSTS.filter((p) => p.category === filter),
    [filter]
  );

  const featured = filtered[0];
  const rest = filtered.slice(1);

  return (
    <PageTransition>
      <section className="relative h-[55vh] min-h-[380px] overflow-hidden flex items-end">
        <img
          src="https://images.pexels.com/photos/11906266/pexels-photo-11906266.jpeg?w=1920"
          alt="Bibliothèque"
          className="absolute inset-0 w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-black/55" />
        <div className="relative z-10 container-luxe pb-16 text-white">
          <p className="text-xs tracking-[0.32em] uppercase mb-4 text-white/80">
            Le Journal
          </p>
          <h1 className="font-display text-6xl sm:text-7xl tracking-tight">
            Bibliothèque
          </h1>
          <p className="mt-4 max-w-xl text-white/85">
            Saisons, événements, portraits et indiscrétions de la maison.
          </p>
        </div>
      </section>

      <section className="py-16 md:py-24 bg-base">
        <div className="container-luxe">
          {/* Filters */}
          <div
            data-testid="blog-filters"
            className="flex flex-wrap gap-2 mb-12"
          >
            {(["Tous", ...BLOG_CATEGORIES] as Filter[]).map((c) => (
              <button
                key={c}
                onClick={() => setFilter(c)}
                data-testid={`blog-filter-${c}`}
                className={`px-4 py-2 text-xs uppercase tracking-[0.18em] rounded-full border transition-all ${
                  filter === c
                    ? "border-strong bg-primary-brand text-white"
                    : "border-subtle text-muted-app hover:border-strong hover:text-primary-app"
                }`}
                style={
                  filter === c
                    ? {
                        backgroundColor: "var(--color-primary)",
                        color: "var(--bg-surface)",
                      }
                    : undefined
                }
              >
                {c}
              </button>
            ))}
          </div>

          {/* Featured */}
          {featured && (
            <motion.article
              key={featured.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
              data-testid={`blog-featured-${featured.id}`}
              className="grid md:grid-cols-2 gap-8 mb-16 group cursor-pointer"
            >
              <div className="relative aspect-[4/3] overflow-hidden rounded-md">
                <img
                  src={featured.image}
                  alt={featured.title}
                  className="img-luxe w-full h-full object-cover transition-transform duration-[1200ms] group-hover:scale-[1.04]"
                />
              </div>
              <div className="flex flex-col justify-center">
                <span className="text-xs tracking-[0.25em] uppercase accent-color mb-4">
                  {featured.category} · {featured.readTime}
                </span>
                <h2 className="font-display text-4xl sm:text-5xl tracking-tight mb-5 leading-tight">
                  {featured.title}
                </h2>
                <p className="text-muted-app text-lg leading-relaxed mb-6">
                  {featured.excerpt}
                </p>
                <div className="flex items-center gap-4 text-xs text-soft-app">
                  <span>{featured.author}</span>
                  <span>·</span>
                  <span>{featured.date}</span>
                </div>
                <button className="mt-8 inline-flex items-center gap-2 text-sm text-primary-app self-start group/btn">
                  Lire l'article
                  <ArrowRight className="h-4 w-4 group-hover/btn:translate-x-1 transition-transform" />
                </button>
              </div>
            </motion.article>
          )}

          {/* Grid */}
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {rest.map((p, idx) => (
              <motion.article
                key={p.id}
                initial={{ opacity: 0, y: 24 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: idx * 0.07 }}
                data-testid={`blog-post-${p.id}`}
                className="group cursor-pointer"
              >
                <div className="relative aspect-[4/3] overflow-hidden rounded-md mb-5">
                  <img
                    src={p.image}
                    alt={p.title}
                    loading="lazy"
                    className="img-luxe w-full h-full object-cover transition-transform duration-[1200ms] group-hover:scale-[1.05]"
                  />
                </div>
                <div className="flex items-center gap-3 text-[11px] tracking-[0.22em] uppercase text-soft-app mb-3">
                  <span className="accent-color">{p.category}</span>
                  <span>·</span>
                  <span>{p.readTime}</span>
                </div>
                <h3 className="font-display text-2xl mb-3 leading-tight group-hover:opacity-80 transition-opacity">
                  {p.title}
                </h3>
                <p className="text-muted-app text-sm leading-relaxed line-clamp-3">
                  {p.excerpt}
                </p>
                <p className="mt-4 text-xs text-soft-app">
                  {p.author} · {p.date}
                </p>
              </motion.article>
            ))}
          </div>
        </div>
      </section>
    </PageTransition>
  );
}
