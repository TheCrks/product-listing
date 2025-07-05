import ColorPicker from "./ColorPicker";
import { fetchProducts } from "../api";
import { useEffect, useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation, Scrollbar, FreeMode } from "swiper/modules";
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/scrollbar';
import "./ProductCard.css";

function ProductCard() {
    const renderStars = (score) => {
        const rating = Math.max(0, Math.min(score * 5, 5)); // Clamp to [0, 5]
        const percentage = (rating / 5) * 100;

        return (
            <div className="star-container" title={rating.toFixed(1) + ' / 5'}>
                <div className="star-back">★★★★★</div>
                <div className="star-front" style={{ width: `${percentage}%` }}>★★★★★</div>
            </div>
        );
    };

    const [productList, setProductList] = useState([]);
    const [selectedColors, setSelectedColors] = useState({});

    useEffect(() => {
        async function loadProducts() {
            try {
                const products = await fetchProducts();
                setProductList(products);

                // Set default selected color to 'yellow'
                const initialColors = {};
                products.forEach((_, index) => {
                    initialColors[index] = 'yellow';
                });
                setSelectedColors(initialColors);
            } catch (error) {
                console.error("Error fetching products:", error);
            }
        }

        loadProducts();
    }, []);

    const handleColorSelect = (index, color) => {
        setSelectedColors((prev) => ({ ...prev, [index]: color }));
    };

    return (
        <div className="product-listing-wrapper">
            <Swiper
                modules={[Navigation, Scrollbar, FreeMode]}
                spaceBetween={20}
                navigation
                scrollbar={{ draggable: true }}
                freeMode={true}
                breakpoints={{
                    0: { slidesPerView: 1 },
                    640: { slidesPerView: 2 },
                    1024: { slidesPerView: 3 },
                    1400: { slidesPerView: 4 },
                }}
                className="product-swiper"
            >
                {productList.map((product, index) => {
                    const selectedColor = selectedColors[index] || 'yellow';

                    return (
                        <SwiperSlide key={index}>
                            <div className="product-card">
                                <img
                                    src={product.images[selectedColor] || "https://via.placeholder.com/150"}
                                    alt={product.name}
                                    className="product-image"
                                />
                                <p className="product-name">{product.name}</p>
                                <p className="product-price">${product.price.toFixed(2)} USD</p>
                                <ColorPicker
                                    selectedColor={selectedColor}
                                    onColorSelect={(color) => handleColorSelect(index, color)}
                                />
                                <div className="popularity">
                                    {renderStars(product.popularityScore)}
                                    <div className="rating-number">
                                        &nbsp;&nbsp;{(product.popularityScore * 5).toFixed(1)}/5
                                    </div>
                                </div>
                            </div>
                        </SwiperSlide>
                    );
                })}
            </Swiper>
        </div>
    );
}

export default ProductCard;
