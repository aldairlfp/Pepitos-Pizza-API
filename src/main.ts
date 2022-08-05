import { NestFactory } from '@nestjs/core';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import { AppModule } from './app.module';
import { ValidationPipe } from '@nestjs/common'
import 'reflect-metadata';
import { DataSource } from 'typeorm';
import { Base } from './base/entities/base.entity';

export const AppDataSource = new DataSource({
  type: 'sqlite',
  database: 'pizzeria.sqlite3',
  entities: [Base],
  synchronize: true,
  logging: false,
});

AppDataSource.initialize()
  .then(() => {
    console.log('Connection with the database succefully');
  })
  .catch((error) => {
    console.log(error);
  });

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.useGlobalPipes(new ValidationPipe());

  const config = new DocumentBuilder()
    .setTitle('Pepitos Pizza API')
    .setDescription('the description of the API')
    .setVersion('1.0')
    .build();

  const document = SwaggerModule.createDocument(app, config);

  SwaggerModule.setup('/documentation', app, document);

  await app.listen(3000);
}
bootstrap();
