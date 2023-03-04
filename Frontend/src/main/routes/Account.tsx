import {Button, Container, Divider, Grid, Link, Paper, Typography} from "@mui/material";
import Routes from "../Routes";

export default function Account() {

    let urls = [
        {
            url: "https://google.com",
            destination: "https://google.com"
        },
        {
            url: "https://google.com",
            destination: "https://google.com"
        },
        {
            url: "https://google.com",
            destination: "https://google.com"
        },
        {
            url: "https://google.com",
            destination: "https://google.com"
        },
        {
            url: "https://google.com",
            destination: "https://google.com"
        }
    ];



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
            <Button color="secondary">
                Logout
            </Button>
            <Link href={Routes.SHORTENER} underline="none">
                <Button sx={{marginTop: 3, marginBottom: 3}} variant="outlined">
                    Add new
                </Button>
            </Link>

            {urls.map(url => {
                return (
                    <Container maxWidth="xl" sx={{marginTop: 1}}>
                        <Grid container rowSpacing={1}>
                            <Grid item xs={4} display="flex" alignItems="center">
                                <Link underline="hover" target="_blank" href={url.url}>
                                    {url.url}
                                </Link>
                            </Grid>
                            <Grid item xs={4} display="flex" alignItems="center">
                                <Link underline="hover" target="_blank" href={url.destination}>
                                    {url.destination}
                                </Link>
                            </Grid>
                            <Grid item xs={4} display="flex" justifyContent="flex-end">
                                <Button id={url.url} variant="outlined" color="secondary">
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