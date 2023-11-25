import React from 'react';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';

import About from './Components/about';
import Home from './Components/homePage';
import Profile from './Components/profile';
import Results from './Components/results';
//TODO these import also required for auth
// import { AuthProvider } from 'react-auth-kit'
// import RouteComponent from './routes';

function App() {
        //TODO when connecting api use these commentd block to authentication
//   <AuthProvider authType = {'cookie'}
//   authName={'_auth'}
//   cookieDomain={window.location.hostname}
//   cookieSecure={window.location.protocol === "https:"}>
// <RouteComponent />
// </AuthProvider>
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/homePage" exact component={Home} />
        <Route path="/about" component={About} />
        <Route path="/profile" component={Profile} />
        <Route path="/results" component={Results} />
      </Switch>
    </Router>
  );
}

export default App;
