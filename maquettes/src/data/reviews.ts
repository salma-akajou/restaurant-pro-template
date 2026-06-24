export type Review = {
  id: string;
  author: string;
  initials: string;
  rating: number;
  quote: string;
  date: string;
  source: "Google" | "TripAdvisor" | "TheFork";
};

export const REVIEWS: Review[] = [
  {
    id: "r1",
    author: "Camille R.",
    initials: "CR",
    rating: 5,
    quote:
      "Un dîner d'anniversaire absolument inoubliable. Le service est d'une précision millimétrique et le wagyu… une révélation.",
    date: "il y a 2 semaines",
    source: "Google",
  },
  {
    id: "r2",
    author: "Mehdi B.",
    initials: "MB",
    rating: 5,
    quote:
      "Le soufflé au chocolat à lui seul vaut le voyage. Une lumière douce, une carte des vins remarquable.",
    date: "il y a 1 mois",
    source: "Google",
  },
  {
    id: "r3",
    author: "Sarah L.",
    initials: "SL",
    rating: 5,
    quote:
      "Chaque assiette est une œuvre. Le chef est passé saluer la table — un moment rare et précieux.",
    date: "il y a 3 semaines",
    source: "TheFork",
  },
  {
    id: "r4",
    author: "Antoine V.",
    initials: "AV",
    rating: 5,
    quote:
      "Maison Lumière coche toutes les cases : décor élégant, cuisine vibrante, accueil chaleureux. À refaire.",
    date: "il y a 5 jours",
    source: "TripAdvisor",
  },
  {
    id: "r5",
    author: "Yasmine T.",
    initials: "YT",
    rating: 5,
    quote:
      "Le menu découverte est un véritable voyage. La burrata à la truffe est inégalée à Casablanca.",
    date: "il y a 2 mois",
    source: "Google",
  },
  {
    id: "r6",
    author: "Léo D.",
    initials: "LD",
    rating: 5,
    quote:
      "Sommelier passionné, accords parfaits, service intuitif. Un cinq étoiles très mérité.",
    date: "il y a 6 semaines",
    source: "Google",
  },
];
