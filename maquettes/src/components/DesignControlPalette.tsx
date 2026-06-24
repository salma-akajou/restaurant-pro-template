import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Sparkles, X, Type } from "lucide-react";
import {
  useTheme,
  ThemeName,
  AccentVariant,
} from "@/contexts/ThemeContext";

const THEMES: { id: ThemeName; label: string; swatches: string[] }[] = [
  {
    id: "light-minimal",
    label: "Light Minimal",
    swatches: ["#FFFFFF", "#2C3531", "#C1A68D"],
  },
  {
    id: "dark-fine-dining",
    label: "Dark Fine Dining",
    swatches: ["#0A0A0A", "#D4AF37", "#6B2D30"],
  },
  {
    id: "pastel-casual",
    label: "Pastel Casual",
    swatches: ["#F4EBE1", "#D26046", "#8FA294"],
  },
];

const ACCENTS: { id: AccentVariant; color: string; label: string }[] = [
  { id: "default", color: "var(--color-accent)", label: "Brand" },
  { id: "amber", color: "#E0A85B", label: "Amber" },
  { id: "rose", color: "#D08089", label: "Rose" },
  { id: "sage", color: "#8FA294", label: "Sage" },
  { id: "indigo", color: "#6A6FB0", label: "Indigo" },
];

export default function DesignControlPalette() {
  const [open, setOpen] = useState(false);
  const { theme, setTheme, headingFont, setHeadingFont, accent, setAccent } =
    useTheme();

  return (
    <>
      <motion.button
        data-testid="design-palette-toggle"
        onClick={() => setOpen((v) => !v)}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        className="fixed bottom-6 right-6 z-50 glass-pill rounded-full px-5 py-3 flex items-center gap-2 shadow-lg"
        aria-label="Open design control palette"
        style={{ boxShadow: "var(--shadow-soft)" }}
      >
        <Sparkles className="h-4 w-4 accent-color" />
        <span className="text-xs tracking-[0.2em] uppercase font-medium">
          Design
        </span>
      </motion.button>

      <AnimatePresence>
        {open && (
          <>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setOpen(false)}
              className="fixed inset-0 z-40 bg-black/20"
            />
            <motion.div
              data-testid="design-palette-panel"
              initial={{ opacity: 0, y: 30, scale: 0.96 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: 30, scale: 0.96 }}
              transition={{ duration: 0.35, ease: [0.2, 0.8, 0.2, 1] }}
              className="fixed bottom-24 right-6 z-50 w-[340px] rounded-2xl bg-surface border border-subtle p-6"
              style={{ boxShadow: "var(--shadow-soft)" }}
            >
              <div className="flex justify-between items-center mb-6">
                <div>
                  <p className="eyebrow">White-Label Studio</p>
                  <h4 className="font-display text-xl mt-1">Design Live</h4>
                </div>
                <button
                  onClick={() => setOpen(false)}
                  className="p-1 rounded-full hover:bg-base"
                  aria-label="Close"
                >
                  <X className="h-4 w-4" />
                </button>
              </div>

              {/* Themes */}
              <div className="mb-6">
                <p className="text-xs uppercase tracking-wider text-muted-app mb-3">
                  Ambiance
                </p>
                <div className="space-y-2">
                  {THEMES.map((t) => (
                    <button
                      key={t.id}
                      data-testid={`theme-option-${t.id}`}
                      onClick={() => setTheme(t.id)}
                      className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg border transition-all ${
                        theme === t.id
                          ? "border-strong bg-base"
                          : "border-subtle hover:border-strong"
                      }`}
                    >
                      <span className="text-sm">{t.label}</span>
                      <div className="flex gap-1">
                        {t.swatches.map((c, i) => (
                          <span
                            key={i}
                            className="w-4 h-4 rounded-full border border-subtle"
                            style={{ backgroundColor: c }}
                          />
                        ))}
                      </div>
                    </button>
                  ))}
                </div>
              </div>

              {/* Typography */}
              <div className="mb-6">
                <p className="text-xs uppercase tracking-wider text-muted-app mb-3">
                  Typographie
                </p>
                <div className="grid grid-cols-2 gap-2">
                  {(["serif", "sans"] as const).map((f) => (
                    <button
                      key={f}
                      data-testid={`heading-font-${f}`}
                      onClick={() => setHeadingFont(f)}
                      className={`px-3 py-2.5 rounded-lg border transition-all flex items-center justify-center gap-2 ${
                        headingFont === f
                          ? "border-strong bg-base"
                          : "border-subtle hover:border-strong"
                      }`}
                    >
                      <Type className="h-3.5 w-3.5" />
                      <span
                        className={`text-base ${
                          f === "serif" ? "font-display" : "font-body"
                        }`}
                      >
                        Aa
                      </span>
                      <span className="text-xs text-muted-app">
                        {f === "serif" ? "Serif" : "Sans"}
                      </span>
                    </button>
                  ))}
                </div>
              </div>

              {/* Accents */}
              <div>
                <p className="text-xs uppercase tracking-wider text-muted-app mb-3">
                  Accent
                </p>
                <div className="flex gap-2 flex-wrap">
                  {ACCENTS.map((a) => (
                    <button
                      key={a.id}
                      data-testid={`accent-${a.id}`}
                      onClick={() => setAccent(a.id)}
                      className={`w-9 h-9 rounded-full border-2 transition-all ${
                        accent === a.id
                          ? "border-primary-brand scale-110"
                          : "border-subtle hover:scale-105"
                      }`}
                      style={{ backgroundColor: a.color }}
                      title={a.label}
                      aria-label={`Accent ${a.label}`}
                    />
                  ))}
                </div>
              </div>

              <p className="mt-6 pt-4 border-t border-subtle text-[11px] text-soft-app leading-relaxed">
                Aperçu temps réel. Toutes les pages s'adaptent instantanément —
                la promesse d'une marque entièrement white-label.
              </p>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </>
  );
}
