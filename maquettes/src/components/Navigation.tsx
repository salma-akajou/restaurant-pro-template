import { NavLink, Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { ShoppingBag, Menu as MenuIcon, X, Sun, Moon } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { useCart } from "@/contexts/CartContext";
import { useTheme } from "@/contexts/ThemeContext";
import { useI18n } from "@/contexts/I18nContext";

const LINKS = [
  { to: "/", labelKey: "nav.home" },
  { to: "/menu", labelKey: "nav.menu" },
  { to: "/bibliotheque", labelKey: "nav.blog" },
  { to: "/about", labelKey: "nav.about" },
];

export default function Navigation() {
  const { count, open } = useCart();
  const { theme, cycleTheme } = useTheme();
  const { lang, setLang, t } = useI18n();
  const [scrolled, setScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      data-testid="nav-header"
      className={`fixed top-0 left-0 right-0 z-40 transition-all duration-500 ${
        scrolled
          ? "py-3 border-b border-subtle"
          : "py-5 border-b border-transparent"
      }`}
      style={{
        backdropFilter: "blur(18px) saturate(180%)",
        WebkitBackdropFilter: "blur(18px) saturate(180%)",
        backgroundColor: scrolled
          ? "color-mix(in srgb, var(--bg-base) 80%, transparent)"
          : "color-mix(in srgb, var(--bg-base) 40%, transparent)",
      }}
    >
      <div className="container-luxe flex items-center justify-between">
        <Link
          to="/"
          data-testid="nav-logo"
          className="flex items-center gap-2 group"
        >
          <span
            className="font-display text-2xl tracking-tight"
            style={{ color: "var(--text-primary)" }}
          >
            Maison
            <span className="italic accent-color"> Lumière</span>
          </span>
        </Link>

        {/* Desktop links */}
        <nav className="hidden md:flex items-center gap-10">
          {LINKS.map((l) => (
            <NavLink
              key={l.to}
              to={l.to}
              end={l.to === "/"}
              data-testid={`nav-link-${l.to.replace("/", "") || "home"}`}
              className={({ isActive }) =>
                `relative text-sm tracking-wide transition-colors ${
                  isActive ? "text-primary-app" : "text-muted-app"
                } hover:text-primary-app`
              }
            >
              {({ isActive }) => (
                <>
                  {t(l.labelKey)}
                  {isActive && (
                    <motion.span
                      layoutId="nav-active"
                      className="absolute -bottom-2 left-0 right-0 h-px"
                      style={{ backgroundColor: "var(--color-accent)" }}
                      transition={{
                        type: "spring",
                        stiffness: 380,
                        damping: 30,
                      }}
                    />
                  )}
                </>
              )}
            </NavLink>
          ))}
        </nav>

        <div className="flex items-center gap-3">
          <button
            data-testid="lang-toggle"
            onClick={() => setLang(lang === "fr" ? "en" : "fr")}
            className="hidden sm:block text-xs tracking-[0.2em] uppercase text-muted-app hover:text-primary-app transition-colors px-2"
            aria-label="Toggle language"
          >
            {lang === "fr" ? "EN" : "FR"}
          </button>

          <button
            data-testid="quick-theme-toggle"
            onClick={cycleTheme}
            className="p-2 rounded-full border border-subtle hover:border-strong transition-colors"
            aria-label="Toggle theme"
            title={`Theme: ${theme}`}
          >
            {theme === "dark-fine-dining" ? (
              <Moon className="h-4 w-4" />
            ) : (
              <Sun className="h-4 w-4" />
            )}
          </button>

          <button
            data-testid="nav-cart-button"
            onClick={open}
            className="relative p-2 rounded-full border border-subtle hover:border-strong transition-colors"
            aria-label="Open cart"
          >
            <ShoppingBag className="h-4 w-4" />
            {count > 0 && (
              <span
                data-testid="cart-count"
                className="absolute -top-1 -right-1 min-w-[18px] h-[18px] px-1 rounded-full text-[10px] font-medium grid place-items-center"
                style={{
                  backgroundColor: "var(--color-primary)",
                  color: "var(--bg-surface)",
                }}
              >
                {count}
              </span>
            )}
          </button>

          <button
            className="md:hidden p-2"
            onClick={() => setMobileOpen((v) => !v)}
            data-testid="mobile-menu-toggle"
            aria-label="Toggle menu"
          >
            {mobileOpen ? (
              <X className="h-5 w-5" />
            ) : (
              <MenuIcon className="h-5 w-5" />
            )}
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.25 }}
            className="md:hidden border-t border-subtle bg-surface"
          >
            <div className="container-luxe py-6 flex flex-col gap-5">
              {LINKS.map((l) => (
                <NavLink
                  key={l.to}
                  to={l.to}
                  end={l.to === "/"}
                  onClick={() => setMobileOpen(false)}
                  data-testid={`mobile-nav-link-${l.to.replace("/", "") || "home"}`}
                  className={({ isActive }) =>
                    `text-2xl font-display ${
                      isActive ? "text-primary-app" : "text-muted-app"
                    }`
                  }
                >
                  {t(l.labelKey)}
                </NavLink>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
