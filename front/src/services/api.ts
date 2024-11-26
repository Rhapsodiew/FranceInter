import axios from 'axios';

const api = axios.create({
 baseURL: 'http://127.0.0.1:8000', // Assurez-vous que l'URL correspond à l'API NestJS
//  withCredentials: true, // Utilisez cette option pour inclure les cookies dans les requêtes
timeout: 20000,
});
export default api