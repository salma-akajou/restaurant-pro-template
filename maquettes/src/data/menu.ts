export type MenuItem = {
  id: string;
  name: string;
  description: string;
  ingredients: string[];
  allergens: string[];
  price: number;
  image: string;
  category: "Entrées" | "Plats" | "Desserts" | "Boissons";
  signature?: boolean;
};

export const MENU: MenuItem[] = [
  {
    id: "burrata-truffle",
    name: "Burrata & Truffe Noire",
    description:
      "Burrata des Pouilles crémeuse, copeaux de truffe noire du Périgord, huile d'olive Frantoia, fleur de sel.",
    ingredients: ["Burrata", "Truffe noire", "Huile d'olive", "Fleur de sel"],
    allergens: ["Lait"],
    price: 24,
    image:
      "https://images.unsplash.com/photo-1616671285410-2a676a9a433d?w=1200&q=85",
    category: "Entrées",
    signature: true,
  },
  {
    id: "tartare-thon",
    name: "Tartare de Thon Rouge",
    description:
      "Thon rouge ligne, avocat hass, sésame torréfié, sauce ponzu maison, pousses de shiso.",
    ingredients: ["Thon rouge", "Avocat", "Ponzu", "Sésame"],
    allergens: ["Poisson", "Sésame"],
    price: 22,
    image:
      "https://images.pexels.com/photos/27774175/pexels-photo-27774175.jpeg?w=1200",
    category: "Entrées",
  },
  {
    id: "veloute-potimarron",
    name: "Velouté de Potimarron",
    description:
      "Potimarron rôti au miel, chantilly de sauge, graines de courge caramélisées.",
    ingredients: ["Potimarron", "Sauge", "Miel", "Graines de courge"],
    allergens: ["Lait"],
    price: 14,
    image:
      "https://images.pexels.com/photos/23644633/pexels-photo-23644633.jpeg?w=1200",
    category: "Entrées",
  },
  {
    id: "boeuf-wagyu",
    name: "Filet de Bœuf Wagyu",
    description:
      "Wagyu A5 saisi à la braise, jus corsé au poivre Sansho, pommes Anna, légumes de saison glacés.",
    ingredients: ["Wagyu A5", "Poivre Sansho", "Pommes de terre", "Légumes"],
    allergens: ["Lait"],
    price: 78,
    image:
      "https://images.unsplash.com/photo-1546964124-0cce460f38ef?w=1200&q=85",
    category: "Plats",
    signature: true,
  },
  {
    id: "saint-pierre",
    name: "Saint-Pierre Rôti",
    description:
      "Saint-Pierre entier rôti sur l'arête, beurre noisette aux câpres, fenouil confit, jus de coquillages.",
    ingredients: ["Saint-Pierre", "Fenouil", "Câpres", "Beurre"],
    allergens: ["Poisson", "Lait"],
    price: 46,
    image:
      "https://images.unsplash.com/photo-1559847844-5315695dadae?w=1200&q=85",
    category: "Plats",
  },
  {
    id: "risotto-cepes",
    name: "Risotto aux Cèpes",
    description:
      "Riz Carnaroli vieilli 24 mois, cèpes des Landes, parmesan Reggiano 36 mois, huile de truffe blanche.",
    ingredients: ["Riz Carnaroli", "Cèpes", "Parmesan", "Truffe blanche"],
    allergens: ["Lait"],
    price: 32,
    image:
      "https://images.unsplash.com/photo-1633964913849-96bb09cfb0fe?w=1200&q=85",
    category: "Plats",
    signature: true,
  },
  {
    id: "souffle-chocolat",
    name: "Soufflé au Chocolat Noir 72%",
    description:
      "Soufflé tiède au chocolat Valrhona, cœur coulant, glace vanille Tahiti, tuile au cacao.",
    ingredients: ["Chocolat Valrhona", "Vanille Tahiti", "Œufs", "Beurre"],
    allergens: ["Lait", "Œufs", "Gluten"],
    price: 16,
    image:
      "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=1200&q=85",
    category: "Desserts",
    signature: true,
  },
  {
    id: "tarte-citron",
    name: "Tarte au Citron de Menton",
    description:
      "Sablé breton, crémeux citron de Menton IGP, meringue italienne brûlée, sorbet basilic.",
    ingredients: ["Citron de Menton", "Beurre", "Œufs", "Basilic"],
    allergens: ["Gluten", "Lait", "Œufs"],
    price: 14,
    image:
      "https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=1200&q=85",
    category: "Desserts",
  },
  {
    id: "ile-flottante",
    name: "Île Flottante Revisitée",
    description:
      "Blanc en neige soufflé, crème anglaise vanille Bourbon, pralin d'amande, caramel à la fleur de sel.",
    ingredients: ["Œufs", "Vanille Bourbon", "Amandes", "Caramel"],
    allergens: ["Lait", "Œufs", "Fruits à coque"],
    price: 13,
    image:
      "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1200&q=85",
    category: "Desserts",
  },
  {
    id: "champagne-coupe",
    name: "Champagne Ruinart Blanc de Blancs",
    description: "Maison Ruinart, 100% Chardonnay, coupe servie à 8°C.",
    ingredients: ["Chardonnay"],
    allergens: ["Sulfites"],
    price: 22,
    image:
      "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=1200&q=85",
    category: "Boissons",
  },
  {
    id: "vin-bordeaux",
    name: "Saint-Émilion Grand Cru 2018",
    description:
      "Domaine Château Figeac, assemblage Merlot/Cabernet Franc, en carafe.",
    ingredients: ["Merlot", "Cabernet Franc"],
    allergens: ["Sulfites"],
    price: 95,
    image:
      "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=1200&q=85",
    category: "Boissons",
  },
  {
    id: "mocktail-jardin",
    name: "Mocktail Jardin Secret",
    description:
      "Concombre, basilic frais, citron vert, eau pétillante, sirop d'agave et fleur de bourrache.",
    ingredients: ["Concombre", "Basilic", "Citron vert", "Agave"],
    allergens: [],
    price: 10,
    image:
      "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=1200&q=85",
    category: "Boissons",
  },
];

export const CATEGORIES: MenuItem["category"][] = [
  "Entrées",
  "Plats",
  "Desserts",
  "Boissons",
];
