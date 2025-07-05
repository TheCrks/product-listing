import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1/fetcher/fetch';

//fetchProducts function to get product data from the API
export const fetchProducts = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};