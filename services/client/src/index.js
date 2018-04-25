
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import registerServiceWorker from './registerServiceWorker';
class App extends Component {    
    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-4">
                        <br/>
                        <h1>All Users</h1>
                        <hr/><br/>
                    </div>
                </div>
            </div>
            )
        }
};
ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();