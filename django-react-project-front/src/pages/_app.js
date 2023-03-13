import '@/styles/globals.css'
import { AppProps } from 'next/app'
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from "../components/Navbar";

axios.defaults.baseURL = 'http://127.0.0.1:8000/';

export default function App({ Component, pageProps }) {
  return (
      <>
        <Navbar />
        <Component {...pageProps} />
      </>
  )
}
