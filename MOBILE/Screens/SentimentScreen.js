import { Image, View, Text, ActivityIndicator, StyleSheet, ScrollView, Linking } from 'react-native';
import React, { useEffect, useState } from 'react';

const SentimentScreen = ({ route }) => {
  console.log(route.params.url)
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(route.params.url);
        const jsonData = await response.json();
        console.log(jsonData)
        setData(jsonData);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchData();

    // Clean up
    return () => {
      // Any cleanup logic if needed
    };
  }, [route.params.url]);

  if (loading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <ActivityIndicator size="large" color="#0000ff" />
      </View>
    );
  }

  if (error) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <Text>Error: {error.message}</Text>
      </View>
    );
  }
  console.log("data:image/png;base64," + data.data);
  // Linking.openURL(`data:image/png;base64,${data.data}`)
  return (
    <ScrollView>
      <View style={{ flex: 1 }}>
        {/* Headline */}
        <Text style={styles.headline}>{data.vibe}</Text>

        {/* Graph (PNG) */}
        <Image source={{ uri: `data:image/png;base64,${data.data}` }} style={styles.graph} />

        {/* Table */}
        <View style={styles.tableContainer}>
          <View style={styles.tableHeader}>
            <Text style={styles.columnHeader}>Neutral Words</Text>
            <Text style={styles.columnHeader}>Positive Words</Text>
            <Text style={styles.columnHeader}>Negative Words</Text>
          </View>
          {data.table.map((rowData, index) => {
            if (!rowData.Negative_Words && !rowData.Positive_Words && !rowData.Positive_Words) {
              return <></>
            }
            return <View style={styles.tableRow} key={index}>
              <Text style={styles.tableCell}>{rowData.Neutral_Words}</Text>
              <Text style={styles.tableCell}>{rowData.Positive_Words}</Text>
              <Text style={styles.tableCell}>{rowData.Negative_Words}</Text>
            </View>
          }


          )}
        </View>
      </View>
    </ScrollView>
  );



}

export default SentimentScreen

const styles = StyleSheet.create({
  headline: {
    fontSize: 20,
    fontWeight: 'bold',
    marginVertical: 10,
    textAlign: 'center',
  },
  graph: {
    width: 400,
    height: 400, // Adjust the height as needed
    // resizeMode: 'contain',
    resizeMode: 'contain'
  },
  tableContainer: {
    marginTop: 20,
    borderWidth: 1,
    borderColor: 'black',
  },
  tableHeader: {
    flexDirection: 'row',
    backgroundColor: 'lightgray',
    padding: 10,
  },
  columnHeader: {
    flex: 1,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  tableRow: {
    flexDirection: 'row',
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: 'lightgray',
  },
  tableCell: {
    flex: 1,
    textAlign: 'center',
    color: 'black', // Text color set to black
  },
});

