import React, { useContext, useState } from "react";
import {Button} from 'react-native'; 

import {
  Dimensions,
  Modal,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from "react-native";
import { NewsContext } from "../API/Context";
import SingleNews from "./SingleNews";
import { Entypo } from "@expo/vector-icons";
import { useLang } from "../API/LangContext";
import {Dropdown} from 'react-native-element-dropdown';



const Search = () => {

  const languageList = [
    { label: 'Arabic', value: 'ar' },
    { label: 'English', value: 'en' },
    { label: 'German', value: 'de' },
    { label: 'French', value: 'fr' },
    { label: 'Spanish', value: 'es' },
    { label: 'Hebrew', value: 'he' },
    { label: 'Italian', value: 'it' }, 
    { label: 'Dutch', value: 'nl' },
    { label: 'Norwegian', value: 'no' }, 
    { label: 'Portuguese', value: 'pt' },
    { label: 'Russian', value: 'ru' }, 
    { label: 'Swedish', value: 'sv' }, 
    { label: 'Chinese', value: 'zh' }, 
  ];
  



  const {
    darkTheme,
    news: { articles },
    setLanguage,
  } = useContext(NewsContext);
  const  {changeLanguage}  = useLang();

  const handleLanguageChange = (newLanguage) => {
    changeLanguage(newLanguage);
  };
  const [searchResults, setSearchResults] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);
  const [currentNews, setCurrentNews] = useState();
  const [selectedlanguage,setSelectedLanguage] = useState('');
  const handleSearch = (text) => {
    if (!text) {
      setSearchResults([]);
      return;
    }
    setSearchResults(articles.filter((query) => query.title.includes(text)));
  };

  const handleModal = (n) => {
    setModalVisible(true);
    setCurrentNews(n);
  };

  const handleDropdownChange = (selectedValue) => {
    console.log(selectedValue);
    setSelectedLanguage(selectedValue.value); 
    console.log(selectedValue.value);
    setLanguage(selectedValue.value); 
  };

  return (
    <View style={{ width: "80%", position: "relative" }}>
      <View style={{display:'flex',flexDirection:'row',justifyContent:'center',}}>
      <TextInput
        style={{
          ...styles.search,
          backgroundColor: darkTheme ? "black" : "lightgrey",
          color: darkTheme ? "white" : "black",
        }}
        onChangeText={(text) => handleSearch(text)}
        placeholder="Search for news"
        placeholderTextColor={darkTheme ? "white" : "grey"}
      />
      {/* <Button title="Change to Spanish" onPress={() => handleLanguageChange('ar')} /> */}
      {/* <Button title="Change to Arabic" onPress={() => setLanguage('ar')} /> */}
      <Dropdown 
      style={styles.dropdown}  
      placeholderStyle={styles.placeholderStyle}       
      selectedTextStyle={styles.placeholderStyle}                          
        searchPlaceholder="Search Languages"
        data={languageList}
        search
        maxWidth={300}  
        maxHeight={300}
        labelField="label"
        valueField="value"
        placeholder="Select Language.."
        value={selectedlanguage}
        onChange={(item) => handleDropdownChange(item)}
      />  
      
      </View>
      <View style={styles.searchResults}>
        {searchResults.slice(0, 10).map((n) => (
          <TouchableOpacity
            key={n.title}
            activeOpacity={0.7}
            onPress={() => handleModal(n)}
          >
            <Text
              style={{
                ...styles.singleResult,
                backgroundColor: darkTheme ? "black" : "white",
                color: darkTheme ? "white" : "black",
              }}
            >
              {n.title}
            </Text>
          </TouchableOpacity>
        ))}
      </View>

      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => {
          setModalVisible(!modalVisible);
        }}
      >
        <TouchableOpacity
          onPress={() => setModalVisible(!modalVisible)}
          style={{
            position: "absolute",
            zIndex: 1,
            right: 0,
            margin: 20,
          }}
        >
          <Entypo name="circle-with-cross" size={30} color="white" />
        </TouchableOpacity>
        <View style={{ height: "100%", transform: [{ scaleY: 1 }] }}>
          <SingleNews item={currentNews} darkTheme={darkTheme} />
        </View>
      </Modal>
    </View>
  );
};

export default Search;

const styles = StyleSheet.create({
  search: {
    paddingVertical: 10,
    paddingHorizontal: 15,
    borderRadius: 10,
    fontSize: 15,
    marginBottom: 15,
  },
  searchResults: {
    position: "absolute",
    zIndex: 1,
    top: 50,
  },
  singleResult: {
    borderRadius: 5,
    padding: 10,
    margin: 0.5,
    shadowColor: "black",
    elevation: 5,
  },
  dropdown: {
    backgroundColor: "#007FFF",
    marginLeft: 10,
    height: 50,
    width: 150,
    borderBottomWidth: 0.5,
    borderWidth: 0.5,
    borderRadius: 8,
    
},
placeholderStyle:{
  color: "white",
  marginLeft: 10,
  textAlign: "center",
}
});