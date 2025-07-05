import ColorPicker from "./ColorPicker";
import { fetchProducts } from "../api";
import { useEffect, useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation, Pagination } from "swiper/modules";
import 'swiper/css'; // Core Swiper styles
import 'swiper/css/navigation';
import 'swiper/css/pagination';

function ProductCard() {
    const [productList, setProductList] = useState([]);

    useEffect(() => {
        async function loadProducts() {
            try {
                const products = await fetchProducts();
                setProductList(products);
            } catch (error) {
                console.error("Error fetching products:", error);
            }
        }

        loadProducts();
    }, []);

    return (
        <div className="product-listing" style={{ width: '1000px', padding: '20px' }}>
            <Swiper
                spaceBetween={20}
                slidesPerView={3}
                navigation
                pagination={{ clickable: true }}
                style={{ width: '1000px' }}
                breakpoints={{
                    640: { slidesPerView: 1 },
                    768: { slidesPerView: 2 },
                    1024: { slidesPerView: 3 },
                }}
                modules={[Navigation, Pagination]}
            >
                {productList.map((product, index) => (
                    <SwiperSlide key={index}>
                        <div className="product-card" style={{ textAlign: 'center' }}>
                            <img
                                src={product.images.yellow || "https://via.placeholder.com/150"}
                                alt={product.name}
                                style={{
                                    width: '200px',
                                    height: '200px',
                                    objectFit: 'cover',
                                    borderRadius: '8px',
                                    margin: '0 auto',
                                }}
                            />
                            <p className="product-name">{product.name}</p>
                            <p className="product-price">${product.price}</p>
                            <ColorPicker />
                            <p className="popularity">Popularity: {product.popularityScore * 5}/5</p>
                        </div>
                    </SwiperSlide>
                ))}
            </Swiper>
        </div>
    );
}

export default ProductCard;
