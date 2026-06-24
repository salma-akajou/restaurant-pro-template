export type GalleryImage = {
  id: string;
  src: string;
  alt: string;
  span: "tall" | "wide" | "square" | "hero";
};

export const GALLERY: GalleryImage[] = [
  {
    id: "g1",
    src: "https://images.pexels.com/photos/11906266/pexels-photo-11906266.jpeg?w=1600",
    alt: "Salle intérieure éclairée",
    span: "hero",
  },
  {
    id: "g2",
    src: "https://images.unsplash.com/photo-1616671285410-2a676a9a433d?w=1000&q=85",
    alt: "Burrata signature",
    span: "tall",
  },
  {
    id: "g3",
    src: "https://images.pexels.com/photos/27774175/pexels-photo-27774175.jpeg?w=1000",
    alt: "Tartare de thon",
    span: "square",
  },
  {
    id: "g4",
    src: "https://images.unsplash.com/photo-1663530761401-15eefb544889?w=1000&q=85",
    alt: "Chef en action",
    span: "wide",
  },
  {
    id: "g5",
    src: "https://images.pexels.com/photos/2977514/pexels-photo-2977514.jpeg?w=1000",
    alt: "Préparation en cuisine",
    span: "square",
  },
  {
    id: "g6",
    src: "https://images.unsplash.com/photo-1559847844-5315695dadae?w=1000&q=85",
    alt: "Poisson rôti",
    span: "square",
  },
  {
    id: "g7",
    src: "https://images.pexels.com/photos/10633476/pexels-photo-10633476.jpeg?w=1600",
    alt: "Décor de table",
    span: "wide",
  },
  {
    id: "g8",
    src: "https://images.pexels.com/photos/4253315/pexels-photo-4253315.jpeg?w=1000",
    alt: "Dressage minutieux",
    span: "tall",
  },
];
