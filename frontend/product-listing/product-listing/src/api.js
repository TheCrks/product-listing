import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL;

//fetchProducts function to get product data from the API
export const fetchProducts = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};