export type BlogPost = {
  id: string;
  title: string;
  excerpt: string;
  category: "Saison" | "Événement" | "Promotion" | "Chef";
  readTime: string;
  image: string;
  date: string;
  author: string;
};

export const BLOG_POSTS: BlogPost[] = [
  {
    id: "automne-2025",
    title: "L'Automne des Sous-Bois",
    excerpt:
      "Le menu d'automne arrive : girolles, châtaignes, gibier d'Auvergne et truffes du Tricastin. Une ode aux forêts françaises.",
    category: "Saison",
    readTime: "5 min",
    image:
      "https://images.pexels.com/photos/23644633/pexels-photo-23644633.jpeg?w=1400",
    date: "12 Oct 2025",
    author: "Chef Hugo Marais",
  },
  {
    id: "soiree-jazz",
    title: "Soirée Jazz & Vins Naturels",
    excerpt:
      "Vendredi 24 novembre — Trio de jazz acoustique, dégustation de 6 vins naturels accordés à un menu en 5 services.",
    category: "Événement",
    readTime: "3 min",
    image:
      "https://images.pexels.com/photos/11906266/pexels-photo-11906266.jpeg?w=1400",
    date: "28 Sep 2025",
    author: "Maison Lumière",
  },
  {
    id: "menu-decouverte",
    title: "Menu Découverte —20% le mardi",
    excerpt:
      "Tous les mardis soirs : le menu Découverte en 7 services est offert à -20%. Réservation conseillée.",
    category: "Promotion",
    readTime: "2 min",
    image:
      "https://images.unsplash.com/photo-1616671285410-2a676a9a433d?w=1400&q=85",
    date: "15 Sep 2025",
    author: "Maison Lumière",
  },
  {
    id: "portrait-chef",
    title: "Portrait : Hugo Marais, l'éloge du geste",
    excerpt:
      "Formé chez Ducasse puis Passard, Hugo Marais raconte son parcours, sa philosophie et ses obsessions végétales.",
    category: "Chef",
    readTime: "8 min",
    image:
      "https://images.unsplash.com/photo-1663530761401-15eefb544889?w=1400&q=85",
    date: "02 Sep 2025",
    author: "Camille Renaud",
  },
  {
    id: "marche-rungis",
    title: "Une nuit à Rungis avec le Chef",
    excerpt:
      "Quatre heures du matin, halles fraîcheur. Reportage immersif sur la sélection quotidienne du Chef.",
    category: "Chef",
    readTime: "10 min",
    image:
      "https://images.pexels.com/photos/4253315/pexels-photo-4253315.jpeg?w=1400",
    date: "20 Aug 2025",
    author: "Camille Renaud",
  },
  {
    id: "saint-valentin",
    title: "Saint-Valentin — Menu à 4 mains",
    excerpt:
      "14 février, dîner exceptionnel à 4 mains avec la cheffe pâtissière Anaïs Diop. Réservation prioritaire ouverte.",
    category: "Événement",
    readTime: "3 min",
    image:
      "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1400&q=85",
    date: "10 Jan 2026",
    author: "Maison Lumière",
  },
];

export const BLOG_CATEGORIES: BlogPost["category"][] = [
  "Saison",
  "Événement",
  "Promotion",
  "Chef",
];
