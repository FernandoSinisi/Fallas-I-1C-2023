import {
    Route,
    Routes,
    BrowserRouter
} from "react-router-dom";

import QuestionPage from "../pages/QuestionPage";

import React from "react";

import {MainContext} from "../services/contexts/MainContext";

const saveQuestion = (question) => {
    localStorage.setItem("question", question);
};

const getQuestion = () => {
    return localStorage.getItem("question");
};

function App() {
    const context = React.useMemo( () => {
            return ( {
                saveQuestion: (question) => saveQuestion(question),

                getQuestion: getQuestion
            } );
        },
        []);

    return (
    <MainContext.Provider value={context}>
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<QuestionPage />} />
        </Routes>
      </BrowserRouter>
    </MainContext.Provider>
    );
}

export default App;
