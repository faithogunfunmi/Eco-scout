import { useState, useEffect } from 'react';
import { Leaf, Search } from 'lucide-react';
import { MOCK_CASES, DEFAULT_RECOMMENDATIONS} from './brandData';
import './App.css';

const translateRating = (number) => {
  if (number === 0) return "Good";
  if (number === 1) return "Bad";
  if (number === 2) return "Mixed";
  return "Unknown";
};


function App() {
  const [activeView, setActiveView] = useState('default'); 
  const [brandData, setBrandData] = useState(null);

  const testBackendConnection = async () => {
      // Step 1a: The hard-coded URL
      console.log("checkpoint1");

      //const fakeUrl = "https://www.shein.com"; 
      //sendUrlToFlask(fakeUrl);

      const sendUrlToFlask = async (liveUrl) => {

      console.log("checkpoint2");

      try {
        // Step 1b: Send the URL to Flask
        console.log(`Sending this URL to Flask: ${liveUrl}`);
        const response = await fetch("http://127.0.0.1:8080", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ url: liveUrl })
        }); 
        
        // Let's print the response so you can prove it worked!
        const data = await response.json();
        console.log("Response from backend:", data);

        if (data && data.overall !== undefined) {
          let viewToTarget = 'default'
          console.log("checkpoint3");
          if (data.overall === 0) {
            setActiveView('yes');
            viewToTarget = 'yes';
            console.log("checkpoint4a");
          } else if (data.overall === 1) {
            viewToTarget = 'no';
            setActiveView('no');
            console.log("checkpoint4b");
          } else if (data.overall === 2) {
            viewToTarget = 'mixed';
            setActiveView('mixed');
            console.log("checkpoint4c");
          }
          else{
            setActiveView('default');
            console.log("checkpoint4d");
          }
        
        setBrandData({
          ...data,
          overall: viewToTarget 
        });
        

        } else {
          setActiveView('default');
          setBrandData(null);
        }

      } catch (error) {
        console.error("Fetch failed. Is Flask running?", error);
        setBrandData(null);
        setActiveView('default');
      }
    };

    // 2. THE MAGIC: Check if we are a real Chrome extension!
   if (typeof chrome !== 'undefined' && chrome.tabs) {
      // We are in Chrome! Grab the active tab URL.
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const liveUrl = tabs[0].url;
        console.log("Live URL from Chrome:", liveUrl);
        sendUrlToFlask(liveUrl); 
      });
    } else {
      // We are just testing on localhost. Use the fake URL so we don't crash.
      console.log("Not in Chrome extension mode. Using test URL.");
      sendUrlToFlask("https://www.shein.com");
    }
    
  };

  useEffect(() => {
    // This function talks to the backend
    console.log("start");
    testBackendConnection();
  }, []); 

  return (


    <div className="app-container">
      {/* HEADER */}


      <header className="header">
  {/* Update the color code here to #345E37 */}
      <Leaf size={24} color="#345E37" /> 
      <h1>EcoScout</h1>
      </header>
  

      {/* --- THE DEFAULT VIEW --- */}
      {activeView === 'default' && (
        <div className="view-container">
          <h2>Scouting for a greener planet.</h2>
          <p className="subtitle">We didn't detect a fast-fashion brand here. Here are some of our favorite sustainable options:</p>
          
          <div className="rec-list">
            {DEFAULT_RECOMMENDATIONS.map((rec, idx) => (
              <div key={idx} className="rec-card">
                <h3>{rec.name}</h3>
                <span className="tag">{rec.type}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* --- THE BRAND VIEWS (Yes, Mixed, No) --- */}
      {activeView !== 'default' && brandData && (
        <div className="view-container">
          <h2 className="brand-title">{brandData.name}</h2>
          
          {/* Ratings Section */}
          <div className="ratings-box">
            <div className="rating-row">
              <span>Ethics Rating:</span>
              <strong>{translateRating(brandData.ethics)}</strong>
            </div>
            <div className="rating-row">
              <span>Sustainability Rating:</span>
              <strong>{translateRating(brandData.sustainability)}</strong>
            </div>
          </div>

          {/* The Visual Meter */}
          <div className="meter-section">
            <div className="meter-container">
              <div className={`meter-arc ${brandData.overall}`}></div>
              <div className={`meter-needle point-${brandData.overall}`}></div>
            </div>
            <div className="meter-labels">
              <span>Good</span>
              <span>Mixed</span>
              <span>Bad</span>
            </div>
          </div>

          {/* Recommendations Box (Only show if there are recommendations) */}
          *{brandData.recommendations?.length > 0 && (
        <div className="rec-box">
          <h3>Recommendations</h3>
          <div className="rec-tags">
            
            {brandData.recommendations.map((recName, idx) => {
              const rawUrl = brandData.recommendURL ? brandData.recommendURL[idx] : "#";

              console.log(`Processing recommendation: ${recName} with URL: ${rawUrl}`);

              // If the URL doesn't start with http, add it!
              const matchingUrl = rawUrl.startsWith('http') ? rawUrl : `https://${rawUrl}`;
              return (
                <a 
                  key={idx} 
                  href={matchingUrl} 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="rec-pill"
                >
                  {recName}
                </a>
              );
            })}

          </div>
        </div>
      )}

      </div> 
    )}

    </div>
  );
}

export default App;
