import { Outlet } from "react-router-dom";
import Navigation from "./Navigation";
import Footer from "./Footer";
import DesignControlPalette from "./DesignControlPalette";
import CartDrawer from "./CartDrawer";

export default function Layout() {
  return (
    <div className="min-h-screen flex flex-col bg-base text-primary-app">
      <Navigation />
      <main className="flex-1 pt-20">
        <Outlet />
      </main>
      <Footer />
      <DesignControlPalette />
      <CartDrawer />
    </div>
  );
}
