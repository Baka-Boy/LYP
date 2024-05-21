import axios from "axios";
import React, { createContext, useEffect, useState } from "react";
import { getNewsAPI, getSourceAPI } from "./api";

export const NewsContext = createContext();

const Context = ({ children }) => {
  const [news, setNews] = useState([]);
  const [category, setCategory] = useState("general");
  const [source, setSource] = useState();
  const [index, setIndex] = useState(0);
  const [darkTheme, setDarkTheme] = useState(true);
  const [language, setLanguage] = useState('en');


  const fetchNews = async (reset = 'general',language = "en") => {
    const { data } = await axios.get(getNewsAPI(reset, 'in',language));

    setNews(data);
    setIndex(1);
  };

  const fetchNewsfromSource = async () => {
    try {
      const { data } = await axios.get(getSourceAPI(source,language));
      setNews(data);
      setIndex(1);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchNews(category,language);
  }, [category,language]);

  useEffect(() => {
    fetchNewsfromSource();
  }, [source,language]);

  return (
    <NewsContext.Provider
      value={{
        news,
        setCategory,
        index,
        setIndex,
        setSource,
        darkTheme,
        setDarkTheme,
        fetchNews,
        language,
        setLanguage,
      }}
    >
      {children}
    </NewsContext.Provider>
  );
};

export default Context;