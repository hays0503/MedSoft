import React from "react";
import "./Home.scss";
import Header from "@components/Header/Header";
import About from "@components/About/About";
import SelectorBody from "@components/SelectorBody/SelectorBody";

const Home: React.FC = () => {
  return (
    <div>
      <Header />
      <div className="Home ">
        <div className="container-fluid">

          <main role="main" className="container mt-5">
            <section id="about">
              <SelectorBody />
              <h2>О Компании МедСофт</h2>
              <p>
                МедСофт — это ведущая компания, специализирующаяся на разработке
                программных решений в области здравоохранения. Наша миссия
                заключается в предоставлении инновационных технологий, которые
                улучшают качество медицинского обслуживания и оптимизируют
                работу медицинских учреждений.
              </p>
            </section>

            <section id="expertise">
              <h3>Наша Экспертиза:</h3>
              <ul className="list-group">
                <li className="list-group-item">
                  Программное обеспечение для медицинских учреждений: Мы
                  разрабатываем и внедряем комплексные информационные системы,
                  включая электронные медицинские карты, системы управления
                  пациентами, расписание приемов, бухгалтерские и
                  административные инструменты.
                </li>
                <li className="list-group-item">
                  Технологии Интеллектуального Анализа Данных: Наши продукты
                  оснащены инструментами искусственного интеллекта и аналитики
                  данных, позволяющими проводить глубокий анализ медицинских
                  данных для выявления закономерностей, предсказания заболеваний
                  и оптимизации лечебных процессов.
                </li>
                <li className="list-group-item">
                  Консалтинг и Поддержка: Мы предоставляем профессиональную
                  консультационную поддержку на всех этапах внедрения наших
                  продуктов, а также обеспечиваем надежную техническую поддержку
                  для бесперебойной работы наших систем.
                </li>
              </ul>
            </section>

            <section id="advantages">
              <h3>Наши Преимущества:</h3>
              <ul className="list-group">
                <li className="list-group-item">
                  Инновационные Решения: Мы постоянно следим за последними
                  тенденциями в области информационных технологий и
                  здравоохранения, чтобы предлагать клиентам передовые решения.
                </li>
                <li className="list-group-item">
                  Надежность и Безопасность: Мы уделяем особое внимание защите
                  данных и обеспечению надежности работы наших систем, чтобы
                  наши клиенты могли быть уверены в безопасности своей
                  информации.
                </li>
                <li className="list-group-item">
                  Гибкость и Настраиваемость: Наши продукты разрабатываются с
                  учетом разнообразных потребностей клиентов, что позволяет нам
                  создавать гибкие и настраиваемые решения для различных
                  медицинских учреждений.
                </li>
              </ul>
            </section>

            <section id="mission">
              <p>
                МедСофт — это партнер, на которого можно полагаться в сфере
                цифровизации здравоохранения. Мы стремимся к тому, чтобы наши
                технологии помогали медицинским учреждениям повышать
                эффективность своей работы и обеспечивать лучшее обслуживание
                пациентов.
              </p>
            </section>
          </main>

          <footer className="footer mt-auto py-3">
            <div className="container">
              <span className="text-muted">МедСофт &copy; 2024</span>
            </div>
          </footer>
        </div>
      </div>
      <About />
    </div>
  );
};

export default Home;
