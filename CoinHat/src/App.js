// import axios from "axios";
import { useEffect, useState } from "react";
import { useRef } from 'react'
import "./App.css";
import Coin from "./components/coinItem/Coin";

function App() {
  const [coins, setCoins] = useState([]);
  const [search, setSearch] = useState("");
  const webSocket = useRef(null);

  useEffect(() => {
    webSocket.current = new WebSocket(`ws://${window.location.hostname}:8000/ws/coins/`);
    webSocket.current.onmessage = (event) => {
      setCoins(JSON.parse(event.data));
      // console.log(coins);
    };
  }, [coins]);

  const handleChange = (e) => {
    setSearch(e.target.value);
  };

  const filteredCoins = coins.filter((coin) =>
    coin.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <div className="header">
        <h1 className="brand">
          <i className="fas fa-hat-cowboy"></i> CoinHat
        </h1>
        <form>
          <input
            className="inputField"
            type="text"
            onChange={handleChange}
            placeholder="Search a Coin"
          />
        </form>
      </div>
      <div className="coinsContainer">
      {filteredCoins.map((coin) => {
          return (
            <Coin
              key={coin.id}
              name={coin.name}
              price={coin.price}
              symbol={coin.symbol}
              marketcap={coin.market_cap}
              volume={coin.total_volume}
              image={coin.image}
              priceChange={coin.price_change_percentage_24h}
            />
          );
        })}
      </div>
    </div>
  );
}

export default App;
