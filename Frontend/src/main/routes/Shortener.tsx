import TextField from "@mui/material/TextField";
import * as React from "react";
import {useState} from "react";
import {Avatar, Button, Container, Link, Typography} from "@mui/material";
import {DirectionsRun} from "@mui/icons-material";
import Routes from "../Routes";

export default function Shortener() {

    const [hasUrl, setHasUrl] = useState(false);
    const [shortened, setShortened] = useState("");

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        let form = new FormData(event.currentTarget);
        setHasUrl(true);
        setShortened("https://google.com");
    };

    const handleNewUrl = () => {
        setHasUrl(false);
        setShortened("");
    }

    return (
        <Container maxWidth="xl" sx={{}}>
            <Container component="main" maxWidth="md" sx={{
                marginTop: 8,
                display: "flex",
                flexDirection: "column",
                alignItems: "center"
            }}
            >
                <Link href={Routes.ACCOUNT}>
                    <Avatar sx={{m: 1, bgcolor: 'secondary.main'}} variant="square">
                        <DirectionsRun
                            color="primary"
                            fontSize="small"
                        />
                    </Avatar>
                </Link>
                <Typography
                    component="h1"
                    variant="h5"
                >
                    Shorten the URL
                </Typography>
                {!hasUrl ?
                    <Container maxWidth="xl">
                        <Container
                            component="form"
                            onSubmit={handleSubmit}
                            maxWidth="xl"
                        >
                            <TextField
                                margin="normal"
                                required
                                fullWidth
                                name="url"
                                label="URL"
                                type="url"
                                id="url"
                            />
                            <Button
                                type="submit"
                                variant="outlined"
                                color="secondary"
                                fullWidth
                            >
                                Shorten
                            </Button>
                        </Container>
                    </Container>
                    :
                    <Container maxWidth="xl">
                        <Link href={shortened} target="_blank">
                            <TextField
                                value={shortened}
                                margin="normal"
                                fullWidth
                                disabled/>
                        </Link>
                        <Button
                            onClick={handleNewUrl}
                            variant="outlined"
                            color="secondary"
                            fullWidth
                        >
                            New URL
                        </Button>
                    </Container>
                }
            </Container>
        </Container>
    );
}