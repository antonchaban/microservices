import {Button, Container, Divider, Grid, Link, Paper, Typography} from "@mui/material";
import Routes from "../routes";
import {useCookies} from "react-cookie";
import Cookies from "../cookies";
import {useNavigate} from "react-router-dom";
import routes from "../routes";
import LinkDTO from "../dto/LinkDTO"
import axios from "../api/client"
import {useEffect, useState} from "react";
import Endpoints from "../api/endpoints";

export default function Account() {

    const [cookies, setCookie, removeCookie] = useCookies();
    const [links, setLinks] = useState<LinkDTO[]>();
    const navigate = useNavigate();

    const userId = cookies[Cookies.USER_ID];
    const accessToken = cookies[Cookies.ACCESS_TOKEN];
    const refreshToken = cookies[Cookies.REFRESH_TOKEN];

    axios.get<LinkDTO[]>(
        Endpoints.PATH_LINKS,
        {
            params: {
                userId: userId
            }
        })
        .then(res => {
            if (res.status !== 200) {
                return;
            }
            let links = res.data.filter(link => link.userId == userId)
            setLinks(links);
        })
        .catch(error => {
            console.error("Error processing links request", error);
        });

    const deleteLink = (id: number|undefined) => {
        axios.delete(`${Endpoints.PATH_LINKS}/${id}`)
            .then(res => {
                if (res.status !== 200) {
                    return;
                }
                setLinks(links?.filter(link => link.id !== id));
            })
            .catch(error => {
                console.error("Error deleting link", error);
            });
    }

    const logout = () => {
        removeCookie(Cookies.USER_ID);
        removeCookie(Cookies.ACCESS_TOKEN);
        removeCookie(Cookies.REFRESH_TOKEN);

        return navigate(routes.LOGIN);
    }

    //init
    useEffect(() => {
        if (!(userId && accessToken)) {
            return navigate(routes.LOGIN);
        }
    }, []);

    return (
        <Container maxWidth="xl" sx={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "space-between",
            marginTop: 8
        }}>
            <Typography variant="h3">
                Username
            </Typography>
            <Button color="secondary" onClick={logout}>
                Logout
            </Button>
            <Link href={Routes.SHORTENER} underline="none">
                <Button sx={{marginTop: 3, marginBottom: 3}} variant="outlined">
                    Add new
                </Button>
            </Link>

            {links?.map(link => {
                return (
                    <Container maxWidth="xl" sx={{marginTop: 1}}>
                        <Grid container rowSpacing={1}>
                            <Grid item xs={3} display="flex" alignItems="center">
                                <Link underline="hover" target="_blank" href={Endpoints.SHORTENER_URL + link.code}>
                                    {link.code}
                                </Link>
                            </Grid>
                            <Grid item xs={3} display="flex" alignItems="center">
                                <Link underline="hover" target="_blank" href={link.url}>
                                    {link.url}
                                </Link>
                            </Grid>
                            <Grid item xs={3} display="flex" alignItems="center" justifyContent="flex-end">
                                <Typography>
                                    {link.expiresStamp || "Permanent"}
                                </Typography>
                            </Grid>
                            <Grid item xs={3} display="flex" justifyContent="flex-end">
                                <Button variant="outlined" color="secondary" onClick={() => deleteLink(link.id)}>
                                    Delete
                                </Button>
                            </Grid>
                        </Grid>
                        <Divider sx={{marginTop: 1}}/>
                    </Container>
                )
            })}
        </Container>
    )
}