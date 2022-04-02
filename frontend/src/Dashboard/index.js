// System imports
import React, { useState, useEffect} from 'react'
import axios from 'axios'
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ReferenceLine,
} from 'recharts';

// Third-party imports (please seek permission before installing other libraries)
import { Accordion, AccordionSummary, AccordionDetails } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

// Image imports
import joel from './joel_cross.jpeg';
import scott from './scott_justason.jpeg';
import tibet from './tibet_cem_gebes.jpeg';
import tyler from './tyler_cowie.jpeg';

import logoImage from './logo_image.png';
import logoText from './logo_text.png';

// Stylesheet import
import './index.scss';

const Dashboard = () => {
    // Please set to unique project identifier (i.e. "energy-dashboard") and do the same in the SCSS file
    let projectName = "Power-Demand-Forecasting"
	
    // API call example to fetch data on page load (sets myData to API response)
    const [myData, setMyData] = useState([])
    useEffect(() => {
        axios.post('http://localhost:8000/predict/')
            .then(response => { setMyData(response.data)}
		)
    }, []);
	
	// Sample data to demostrate the recharts library functionality
    const data = [
        {
            "name": "0:00",
            "Forecasted Demand": myData[0],
            "Real Demand": 40,
        },
        {
            "name": "1:00",
            "Forecasted Demand": myData[1],
            "Real Demand": 41,
        },
        {
            "name": "3:00",
            "Forecasted Demand": myData[2],
            "Real Demand": 42,
        },
        {
            "name": "4:00",
            "Forecasted Demand": myData[3],
            "Real Demand": 43,
        },
        {
            "name": "5:00",
            "Forecasted Demand": myData[4],
            "Real Demand": 44,
        },
        {
            "name": "6:00",
            "Forecasted Demand": myData[5],
            "Real Demand": 45,
        },
        {
            "name": "7:00",
            "Forecasted Demand": myData[6],
            "Real Demand": 46,
          
        },
		{
            "name": "8:00",
            "Forecasted Demand": myData[7],
            "Real Demand": 47,
          
        },
		{
            "name": "9:00",
            "Forecasted Demand": myData[8],
            "Real Demand": 48,
            
        },
		{
            "name": "10:00",
            "Forecasted Demand": myData[9],
            "Real Demand": 49,
           
        },
		{
            "name": "11:00",
            "Forecasted Demand": myData[10],
            "Real Demand": 410,
           
        },
		{
            "name": "12:00",
            "Forecasted Demand": myData[11],
            "Real Demand": 411,
          
        },
		{
            "name": "13:00",
            "Forecasted Demand": myData[12],
            "Real Demand": 40,

        },
		{
            "name": "14:00",
            "Forecasted Demand": myData[13],
            "Real Demand": 40,

        },
		{
            "name": "15:00",
            "Forecasted Demand": myData[14],
            "Real Demand": 40,

        },
		{
            "name": "16:00",
            "Forecasted Demand": myData[15],
            "Real Demand": 40,
        },
		{
            "name": "17:00",
            "Forecasted Demand": myData[16],
            "Real Demand": 40,
        },
		{
            "name": "18:00",
            "Forecasted Demand": myData[17],
            "Real Demand": 40,
        },
		{
            "name": "19:00",
            "Forecasted Demand": myData[18],
            "Real Demand": 40,
        },
		{
            "name": "20:00",
            "Forecasted Demand": myData[19],
            "Real Demand": 40,
        },
		{
            "name": "21:00",
            "Forecasted Demand": myData[20],
            "Real Demand": 40,
        },
		{
            "name": "22:00",
            "Forecasted Demand": myData[21],
            "Real Demand": 40,
        },
		{
            "name": "23:00",
            "Forecasted Demand": myData[22],
            "Real Demand": 40,
        },
		{
            "name": "24:00",
            "Forecasted Demand": myData[23],
            "Real Demand": 40,
        },
    ]

    return (
        // Page content container
        <div className={`${projectName}`}>

            {/* Back button */}
            <span className={`${projectName}__back`}>
                <a href='/'>&lt; Back</a>
            </span>

            {/* Page header */}
            <div className={`${projectName}__header`}>
                <div className={`${projectName}__header-rows`}>
                    <div className={`${projectName}__header-top-row`}>
                        <img className={`${projectName}__header-logo-image`} src={logoImage} />
                        <img className={`${projectName}__header-logo-text`} src={logoText} />
                        <div className={`${projectName}__header-top-row-divider`}><p>|</p></div>
                        <div className={`${projectName}__header-top-row-text`}><p>Design</p></div>
                    </div>
                    <div className={`${projectName}__header-bottom-row`}>
                        <p>Energy Demand Forecasting</p>
                    </div>
                </div>
            </div>

            {/* TEAM MEMBERS TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Team Members
                </AccordionSummary>
                <AccordionDetails>
                    <div className={`${projectName}__team-member`}>
                        {/* Tyler */}
                        <div className={`${projectName}__team-member-wrapper`}>
                            <img className={`${projectName}__team-member-headshot`} src={tyler} />
                            <p className={`${projectName}__team-member-name`}>Tyler Cowie</p>
                            <p>3rd Year Electrical Engineering</p>
                            <a href="https://www.linkedin.com/in/cowiety/">LinkedIn</a>
                        </div>
                        {/* Joel */}
                        <div className={`${projectName}__team-member-wrapper`}>
                            <img className={`${projectName}__team-member-headshot`} src={joel} />
                            <p className={`${projectName}__team-member-name`}>Joel Cross</p>
                            <p>4th Year Computing</p>
                            <a href="https://www.linkedin.com/in/joeldcross/">LinkedIn</a>
                        </div>
                        {/* Tibet */}
                        <div className={`${projectName}__team-member-wrapper`}>
                            <img className={`${projectName}__team-member-headshot`} src={tibet} />
                            <p className={`${projectName}__team-member-name`}>Tibet Cem Gebes</p>
                            <p>4th Year Philosophy</p>
                            <a href="https://www.linkedin.com/in/tibet-cem-gebes-932431127/">LinkedIn</a>
                        </div>
                        {/* Scott */}
                        <div className={`${projectName}__team-member-wrapper`}>
                            <img className={`${projectName}__team-member-headshot`} src={scott} />
                            <p className={`${projectName}__team-member-name`}>Scott Justason</p>
                            <p>3rd Year Apple Math (Comp)</p>
                            <a href="https://www.linkedin.com/in/scott-justason-823b91209/">LinkedIn</a>
                        </div>
                    </div>
                </AccordionDetails>
            </Accordion>

            {/* PROJECT DESCRIPTION TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Project Description
                </AccordionSummary>
                <AccordionDetails>
                    The amount of energy drawn from the power grid can be unpredictable. Analogous to the stock market, Ontario’s energy demand causes fluctuations in its cost throughout the day. To manage this demand, Ontario’s grid operator has incentives in place for limiting power consumption during peak demand hours. Queen’s University aims to meet these incentives by using their behind-the-meter generation while demand is high. By minimizing the power drawn from the grid at the right times, Queen’s University can potentially save $1M annually. However, electricity demand is influenced by a variety of factors, such as the season, temperature and day of the week. The goal of this work is to consider these factors in a recursive neural network to predict the times of peak electricity demand. The team will implement this model in a dashboard, allowing Queen’s Energy Management to determine when peak demand is most likely each day.
                </AccordionDetails>
            </Accordion>

            {/* DATA TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Our Data
                </AccordionSummary>
                <AccordionDetails>
                    A substantial portion of Ontario’s energy demand is dependent on the weather. After researching the correlation between historical weather data and energy demand, it became obvious that the price of electricity is sensitive to short-term fluctuations in climate or weather conditions. Because of this fact the dominating piece of data driving our LSTM model is weather data collected from the 10 most populous cities in Ontario from an OpenWeather API. The historical data from these 10 cities was combined into a weighted average that we used to train our model. After testing this model just using weather data, we found that it was already more accurate than a statistical ARIMA model. To make further improvements, we added holiday data to our model as we found that also had an impact on energy demand for a given day. If we were to continue this project, we could do more research on how factors impacting energy demand and include them in our model's testing dataset.
                </AccordionDetails>
            </Accordion>

            {/* MODEL TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Our Model
                </AccordionSummary>
                <AccordionDetails>
                    A typical RNN doesn’t carry the past influences in their 'raw' potentials; rather, with each set of inputs, a value loses its influence. Conversely, in our LSTM model, each LSTM cell considers a secondary value descending from the previous neuron. This is achieved through the implementation of a new input: a memory input. In an LSTM model, two inputs (input t and output t-1) are inserted into the activation function, which enables the model to have long-term memory. This memory could allow the model to remember important relationships, such as the gender of a subject or a vector of sequential data. When the model encounters something new that's relevant, it will reconsider what has been memorized thus far to produce a more accurate output. The LSTM implements this by decreasing the influence of older inputs in favour of the more recent observation.
                </AccordionDetails>
            </Accordion>

            {/* DEMO TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Demo
                </AccordionSummary>
                <AccordionDetails>
                    <div className={`${projectName}__demo`}>
                        <div className={`${projectName}__demo-chart-container`}>
                            <p className={`${projectName}__demo-chart-title`}>Ontario Energy Demand</p>
                            <p className={`${projectName}__demo-chart-desc`}>This plot compares what our AI model predicts the demand to be with the actual values. </p>
                            <LineChart
							  width={800}
							  height={300}
							  data={data}
							  margin={{
								top: 20,
								right: 50,
								left: 20,
								bottom: 5,
							  }}
							>
							  <CartesianGrid strokeDasharray="3 3" />
							  <XAxis dataKey="name" />
							  <YAxis type="number" domain={[10000, 30000]} />
							  <Tooltip />
							  <Legend />
							  <ReferenceLine y={22000} label="Very High Demand" stroke="red" />
							  <Line type="monotone" dataKey="Forecasted Demand" stroke="#8884d8" />
							  <Line type="monotone" dataKey="Real Demand" stroke="#82ca9d" />
							</LineChart>
                        </div>
                    </div>
                </AccordionDetails>
            </Accordion>
			
        </div>
    );
}

// Please change to component name decided upon at top of the code
export default Dashboard;
