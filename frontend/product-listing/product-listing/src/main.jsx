import { StrictMode, useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import ProductCard from './components/ProductCard.jsx';
import './fonts.css';
import { fetchProducts } from './api';

function App() {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        async function load() {
            try {
                const res = await fetchProducts();
                setProducts(res);
            } catch (err) {
                console.error("Error loading products:", err);
                setError(true);
            } finally {
                setLoading(false);
            }
        }
        load();
    }, []);

    let headerText = "Product List";
    if (loading) headerText = "Loading...";
    else if (error) headerText = "Error loading products";

    return (
        <>
            <p className="page-header">{headerText}</p>
            {!error && <ProductCard products={products} />}
        </>
    );
}

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <App />
    </StrictMode>
);
