import { useLang } from "./LangContext";


export const categories = [
  {
    code: "",
    pic: "https://img.icons8.com/fluent/96/000000/news.png",
    name: "general",
  },
  {
    code: "",
    pic: "https://img.icons8.com/fluent/96/000000/hard-working.png",
    name: "business",
  },
  {
    code: "",
    pic: "https://img.icons8.com/fluent/96/000000/movie-projector.png",
    name: "entertainment",
  },
  {
    pic: "https://img.icons8.com/fluent/96/000000/stethoscope.png",
    name: "health",
  },
  {
    pic: "https://img.icons8.com/fluent/96/000000/microscope.png",
    name: "science",
  },
  {
    pic: "https://img.icons8.com/fluent/96/000000/trophy.png",
    name: "sports",
  },
  {
    pic: "https://img.icons8.com/fluent/96/000000/artificial-intelligence.png",
    name: "technology",
  },
];

export const country = [
  {
    code: "in",
    name: "India",
  },
  {
    code: "us",
    name: "USA",
  },
  {
    code: "au",
    name: "Australia",
  },
  {
    code: "ru",
    name: "Russia",
  },
  {
    code: "fr",
    name: "France",
  },
  {
    code: "gb",
    name: "United Kingdom",
  },
];

export const sources = [
  {
    id: "bbc-news",
    name: "BBC News",
    pic: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/BBC_News_2019.svg/1200px-BBC_News_2019.svg.png",
    domain: "bbc.com"
  },
  {
    id: "cnn",
    name: "CNN",
    pic: "https://upload.wikimedia.org/wikipedia/commons/f/fb/Cnn_logo_red_background.png",
    domain: "cnn.com"
  },
  {
    id: "fox-news",
    name: "Fox News",
    domain: "foxnews.com",
    pic: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/768px-Fox_News_Channel_logo.svg.png",
  },
  {
    id: "google-news",
    name: "NBC News",
    domain: "nbcnews.com",
    pic: "https://upload.wikimedia.org/wikipedia/commons/archive/9/9f/20140917183018%21NBC_News_2013_logo.png",
  },
];

export const BASE_URL = "https://newsapi.org/v2/";
export const apikey = 'e9428d85ff1a4df8994ed6e978827bf4'
export const backend_link = 'https://aed3-2401-4900-172d-fd6a-88b5-2618-b17e-25a4.ngrok-free.app';

export const getNewsAPI = (category, country = "in",language) => {
  // const {lang} = useLang();
  return `${BASE_URL}/top-headlines/?category=${category}&?country=${country}&apiKey=${apikey}&language=${language}`;
};


export const getSourceAPI = (source,language) => {
  return `${BASE_URL}/everything?domains=${source}&apiKey=${apikey}&language=${language}`;
};

