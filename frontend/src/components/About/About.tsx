import React from "react";
import "./About.scss";
import MedSoft from "@img/MedSoft.png";

const About: React.FC = () => {
  return (
    <footer 
    // className="fixed-bottom "
    >
      <div className="About bg-dark bg-gradient text-white">
        <img src={MedSoft}/>
        <h5>О нас</h5>
        <p>
          МедСофт — это ведущая компания, специализирующаяся на разработке
          программных решений в области здравоохранения. Наша миссия заключается
          в предоставлении инновационных технологий, которые улучшают качество
          медицинского обслуживания и оптимизируют работу медицинских
          учреждений.
        </p>
      </div>      

    </footer>
  );
};

export default About;
