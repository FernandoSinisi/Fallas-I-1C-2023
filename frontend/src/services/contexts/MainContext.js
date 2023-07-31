import React from 'react'

const MainContext = React.createContext(undefined);

export {
    MainContext
};

export function useMainContext() {
    const context = React.useContext(MainContext);

    if (! context){
        throw new Error("Error de contexto.");
    }

    return context;
}
