import { Routes, Route, useLocation } from "react-router-dom";
import { AnimatePresence } from "framer-motion";
import { Toaster } from "@/components/ui/sonner";
import { ThemeProvider } from "@/contexts/ThemeContext";
import { CartProvider } from "@/contexts/CartContext";
import { I18nProvider } from "@/contexts/I18nContext";
import Layout from "@/components/Layout";
import Home from "@/pages/Home";
import MenuPage from "@/pages/Menu";
import Blog from "@/pages/Blog";
import About from "@/pages/About";
import NotFound from "@/pages/NotFound";

export default function App() {
  const location = useLocation();
  return (
    <I18nProvider>
      <ThemeProvider>
        <CartProvider>
          <AnimatePresence mode="wait">
            <Routes location={location} key={location.pathname}>
              <Route element={<Layout />}>
                <Route index element={<Home />} />
                <Route path="/menu" element={<MenuPage />} />
                <Route path="/bibliotheque" element={<Blog />} />
                <Route path="/about" element={<About />} />
                <Route path="*" element={<NotFound />} />
              </Route>
            </Routes>
          </AnimatePresence>
          <Toaster position="bottom-center" />
        </CartProvider>
      </ThemeProvider>
    </I18nProvider>
  );
}
