import React, {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
} from "react";

export type ThemeName = "light-minimal" | "dark-fine-dining" | "pastel-casual";
export type HeadingFont = "serif" | "sans";
export type AccentVariant = "default" | "amber" | "rose" | "sage" | "indigo";

type ThemeContextValue = {
  theme: ThemeName;
  setTheme: (t: ThemeName) => void;
  headingFont: HeadingFont;
  setHeadingFont: (f: HeadingFont) => void;
  accent: AccentVariant;
  setAccent: (a: AccentVariant) => void;
  cycleTheme: () => void;
};

const ThemeContext = createContext<ThemeContextValue | null>(null);

const STORAGE_KEY = "restoflex.theme.v1";

const ACCENT_OVERRIDES: Record<AccentVariant, string | null> = {
  default: null,
  amber: "#E0A85B",
  rose: "#D08089",
  sage: "#8FA294",
  indigo: "#6A6FB0",
};

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setThemeState] = useState<ThemeName>("light-minimal");
  const [headingFont, setHeadingFontState] = useState<HeadingFont>("serif");
  const [accent, setAccentState] = useState<AccentVariant>("default");

  useEffect(() => {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        if (parsed.theme) setThemeState(parsed.theme);
        if (parsed.headingFont) setHeadingFontState(parsed.headingFont);
        if (parsed.accent) setAccentState(parsed.accent);
      }
    } catch {}
  }, []);

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
    document.documentElement.setAttribute("data-heading-font", headingFont);

    const override = ACCENT_OVERRIDES[accent];
    if (override) {
      document.documentElement.style.setProperty("--color-accent", override);
    } else {
      document.documentElement.style.removeProperty("--color-accent");
    }

    try {
      localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({ theme, headingFont, accent })
      );
    } catch {}
  }, [theme, headingFont, accent]);

  const value = useMemo<ThemeContextValue>(
    () => ({
      theme,
      setTheme: setThemeState,
      headingFont,
      setHeadingFont: setHeadingFontState,
      accent,
      setAccent: setAccentState,
      cycleTheme: () => {
        const order: ThemeName[] = [
          "light-minimal",
          "dark-fine-dining",
          "pastel-casual",
        ];
        const idx = order.indexOf(theme);
        setThemeState(order[(idx + 1) % order.length]);
      },
    }),
    [theme, headingFont, accent]
  );

  return (
    <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
  );
}

export function useTheme() {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used within ThemeProvider");
  return ctx;
}
