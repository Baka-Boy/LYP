import React, { useContext,useState } from "react";
import { StatusBar, StyleSheet, View } from "react-native";
import Context, { NewsContext } from "./API/Context";
import Apptabs from "./components/apptabs";
import { NavigationContainer } from '@react-navigation/native';
import { LangProvider } from "./API/LangContext";
import LangContext from "./API/LangContext";
function App() {
  const { darkTheme } = useContext(NewsContext);

  return (
    <View
      style={{
        ...styles.container,
        backgroundColor: darkTheme ? "#282C35" : "white",
      }}
    >
      <NavigationContainer>
      <Apptabs />
      </NavigationContainer>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: StatusBar.currentHeight,
  },
});

export default () => {
  const [language,setLanguage] = useState('en');

  const changeLanguage = (language) => {
    setLanguage(language);
  };
  return (
    <Context>
      {/* <LangProvider> */}
      {/* <LangContext.Provider value={{language,changeLanguage}}> */}
        <App />
      {/* </LangProvider> */}
      {/* </LangContext.Provider> */}
    </Context>
  );
};