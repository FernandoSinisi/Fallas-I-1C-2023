import React from 'react';

import {
    Button, FormControl, FormControlLabel,
    Radio, RadioGroup, Typography, Box
} from '@mui/material';

import {postTo} from "../helpers/RequestHelper";

import {BlankLine} from "../components/BlankLine";

import {DIAGNOSTIC_PATH} from "../constants/constants";

import { createTheme, ThemeProvider } from '@mui/material/styles';

import { styled } from '@mui/system';

import ReactHtmlParser from "react-html-parser";

import {useMainContext} from "../services/contexts/MainContext";

const ImageContainer = styled(Box)({
    display: 'flex',
    justifyContent: 'center',
    marginTop: '1rem',
});

const StyledImage = styled('img')({
    maxWidth: '9%',
    height: 'auto',
});

const TitleTypography = styled(Typography)(({ theme }) => ({
    fontSize: '2.5rem',
    fontWeight: 'bold',
    color: 'black',
    marginBottom: theme.spacing(2),
    fontFamily: 'EB Garamond, serif',
}));

const theme = createTheme({
    palette: {
        primary: {
            main: '#ecac3b',
        },
    },
});

const QuestionPage = () => {
    const [currentQuestion, setCurrentQuestion] = React.useState("");

    const [options, setOptions] = React.useState([]);

    const [selectedOption, setSelectedOption] = React.useState("");

    const [nextTag, setNextTag] = React.useState("");

    const [restart, setRestart] = React.useState(true);

    const [showButton, setShowButton] = React.useState(true);

    const [answers, setAnswers] = React.useState({});

    const {saveQuestion, getQuestion} = useMainContext();

    const [updatedQuestions, setUpdatedQuestions] = React.useState([]);

    const handleContinue = async () => {
        try {
            if (! restart) {
                const newAnswers = answers;

                newAnswers[nextTag] = selectedOption;

                setAnswers(newAnswers);
            }

            const response = await postTo(`${process.env.REACT_APP_BACKEND_HOST}${DIAGNOSTIC_PATH}`, answers);

            setRestart(false);

            const {
                next_tag,
                questions,
                diagnostic
            } = response;

            if (!next_tag) {
                setCurrentQuestion(diagnostic);

                setShowButton(false);

                setOptions([]);
            } else {
                saveQuestion(next_tag);

                setNextTag(getQuestion());

                setCurrentQuestion(questions[next_tag].question);

                setUpdatedQuestions(questions);

                setOptions(questions[next_tag].options);
            }
            setSelectedOption('');
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const handleRestart = () => {
        window.location.reload();
    }

    React.useEffect(() => {
        handleContinue().then();
    }, [])

    return (
        <Box backgroundColor="#f2f2f2">
        <BlankLine number={5}/>

        <ThemeProvider theme={theme}>
            <Box textAlign="center">
                <TitleTypography variant="h3" gutterBottom>
                    Diagnóstico de Hipertiroidismo
                </TitleTypography>

                <ImageContainer>
                    <StyledImage
                        src="https://firebasestorage.googleapis.com/v0/b/ticketapp-firebase.appspot.com/o/health.png?alt=media&token=b9f6248b-43e7-4d14-9ab3-37e8703cd62c&_gl=1*8zm441*_ga*Mzg5NjM0MjcuMTY1NjEwMjEwNQ..*_ga_CW55HF8NVT*MTY4NjU4ODMzNS40NC4xLjE2ODY1ODgzOTcuMC4wLjA."
                        alt="Image" />
                </ImageContainer>
            </Box>

            <BlankLine number={2}/>
        </ThemeProvider>

        <Box
            display="flex"
            flexDirection="column"
            padding="2rem"
            boxShadow="0 0 10px rgba(0, 0, 0, 0.1)"
            borderRadius="8px"
            backgroundColor="#ffffff"
            width="60%"
            margin="0 auto"
        >
            <Box
                display="flex"
                flexDirection="column"
                alignItems="flex-start"
                width="100%"
            >
                <BlankLine/>


                {
                    (showButton) && (
                        <Box width="100%">
                            <Typography variant="h6" gutterBottom>
                                {currentQuestion}
                            </Typography>
                        </Box>
                    )
                }



                {
                    (! showButton) && (
                        <Box width="100%">
                            <div>{ReactHtmlParser(currentQuestion)}
                            </div>
                        </Box>
                    )
                }
            </Box>

            <Box marginTop="1rem">
                <FormControl component="fieldset">
                    <RadioGroup
                        value={selectedOption}
                        onChange={(e) => setSelectedOption(e.target.value)}
                    >
                        {options.map((option, index) => (
                            <FormControlLabel
                                key={index}
                                value={option}
                                control={<Radio />}
                                label={option}
                            />
                        ))}
                    </RadioGroup>
                </FormControl>
            </Box>

            {
                (showButton) ? (
                    <Box marginTop="1rem">
                        <Button variant="contained" onClick={handleContinue}>
                            Siguiente
                        </Button>
                    </Box>
                ) : (
                    <Box marginTop="1rem">
                        <Button variant="contained" onClick={handleRestart}>
                            Empezar otra vez
                        </Button>
                    </Box>
                )
            }
        </Box>

        <BlankLine number={22}/>
        </Box>
    );
};

export default QuestionPage;