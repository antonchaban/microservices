import React, {useEffect} from 'react';
import {useCookies} from "react-cookie";
import {useNavigate} from "react-router-dom";
import Routes from "../Routes";

export default function App() {

    const [cookies, setCookie, removeCookie] = useCookies();
    const navigate = useNavigate();

    let session = cookies['session'];

    useEffect(() => {
        if (session) {
            removeCookie('session');
            return navigate(Routes.SHORTENER);
        }
        return navigate(Routes.LOGIN);
    }, [])

    return (
     <div/>
    );

}
