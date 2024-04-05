/**
 * Contains the miscellaneous route handlers.
 * @author Rosemond Asilga <https://github.com/rosemondasilga>
 */
class AppController {
    static getHomepage(request, response) {
      response.status(200).send('Hello Holberton School!');
    }
  }
  
  export default AppController;
  module.exports = AppController;