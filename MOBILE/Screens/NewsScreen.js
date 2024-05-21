import React, { useContext, useState } from "react";
import {
  Dimensions,
  Text,
  View,
  StyleSheet,
  TouchableOpacity,
  Linking
} from "react-native";
import Carousel from "react-native-snap-carousel";
import { NewsContext } from "../API/Context";
import SingleNews from "../components/SingleNews";
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import SentimentScreen from "./SentimentScreen";
import ChatScreen from "./ChatScreen";
import { backend_link } from "../API/api";
import { useLang } from '../API/LangContext';



const NewsScreenInside = ({navigation}) => {
  const {
    news: { articles },
    darkTheme,
  } = useContext(NewsContext);

  const [activeIndex, setActiveIndex] = useState(0);

  const windowHeight = Dimensions.get("window").height;  return (
    <View style={styles.carousel}>
      {articles && (
        <Carousel
          firstItem={activeIndex}
          layout={"stack"}
          data={articles.slice(0, 20)}
          sliderHeight={300}
          itemHeight={windowHeight}
          vertical={true}
          renderItem={({ item, index }) => (
            <SingleNews item={item} index={index} darkTheme={darkTheme} />
          )}
          onSnapToItem={(index) => setActiveIndex(index)}
        />
      )}
      <TouchableOpacity
        onPress={() => {
          if (articles && articles[activeIndex]) {
            navigation.navigate('SentimentScreen',{url:
              backend_link + '/api?url=' + new URL(articles[activeIndex].url).toString()
            })
            // Linking.openURL('https://e646-2409-4080-d14-7827-d14a-e217-4bbb-6484.ngrok-free.app/api?url=' + new URL(articles[activeIndex].url).toString());

          }
        }}
        style={{ backgroundColor: '#007FFF', padding: 10 }}
      >
        <Text style={{textAlign: 'center', color: 'white',backgroundColor:'#007FFF' }}>Conduct Sentiment Analysis</Text>

      </TouchableOpacity>

      {/* <TouchableOpacity
        onPress={() => {
          if (articles && articles[activeIndex]) {
            navigation.navigate('ChatScreen',{url:
              backend_link + '/chatcontent?url=' + new URL(articles[activeIndex].url).toString()
            })
            // Linking.openURL('https://e646-2409-4080-d14-7827-d14a-e217-4bbb-6484.ngrok-free.app/api?url=' + new URL(articles[activeIndex].url).toString());

          }
        }}
        style={{ backgroundColor: '#007FFF', padding: 10 }}
      >
        <Text style={{textAlign: 'center', color: 'white',backgroundColor:'#007FFF' }}>Ask Questions</Text>

      </TouchableOpacity> */}
      
    </View>
  );
}

const NewsScreen = () => {

  // const { lang, setLang } = useLang();

  // const changeLang = () => {
  //   // Example function to change the lang
  //   setLang('fr');
  // };



  // console.log(articles && articles[9]);
  const Stack = createNativeStackNavigator();

  return (
    <Stack.Navigator>
      <Stack.Screen name="NewsScreen" component={NewsScreenInside} options={{ headerShown: false }} />
      <Stack.Screen name="SentimentScreen" component={SentimentScreen} options={{ headerShown: false }}/>
      <Stack.Screen name="ChatScreen" component={ChatScreen} options={{ headerShown: false }}/>
    </Stack.Navigator>
  );
};

export default NewsScreen;

const styles = StyleSheet.create({
  carousel: {
    flex: 1,
    // transform: [{ scaleY: -1 }],
    backgroundColor: "black",
  },
});