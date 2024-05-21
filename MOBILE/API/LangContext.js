import React, { createContext, useContext, useState } from 'react';

// Create a context for lang
const LangContext = createContext('en');
export default LangContext;
// Create a custom hook to use the language context
export const useLanguage = () => useContext(LangContext);
// Custom hook to use lang context
export const useLang = () => {
  return useContext(LangContext);
};
// Create a provider component
export const LangProvider = ({ children }) => {
  const [lang, setLang] = useState('en');
  const changeLanguage = (newLanguage) => {
    setLang(newLanguage);
  };
  return (
    <LangContext.Provider value={{ lang, changeLanguage }}>
      {children}
    </LangContext.Provider>
  );
};

